from broadlink_client import BroadlinkClient
from song import Song
import time
from pydub import AudioSegment
import threading
import pygame

class SongPlayer:
    def __init__(self, latency_compensation=0.12):
        self.broadlink_client = BroadlinkClient()
        self.latency_compensation = latency_compensation

    @staticmethod
    def generate_beats(song_duration, bpm, start_offset=0):
        """Generate beat times based on BPM instead of audio analysis"""
        beat_interval = 60.0 / bpm
        beats = []
        current_time = start_offset
        
        while current_time < song_duration:
            beats.append(current_time)
            current_time += beat_interval
        
        return beats

    def play(self, song: Song):
         # Get song duration and generate beats based on BPM
        song_audio = AudioSegment.from_wav(song.audio_wav_path)
        song_duration = len(song_audio) / 1000.0
        beats = self.generate_beats(song_duration, song.bpm, start_offset=song.first_beat_offset_seconds)

        # Initialize pygame mixer for audio playback
        pygame.mixer.init()
        
        # Play the song in a separate thread using pygame for better sync
        def play_song():
            pygame.mixer.music.load(song.audio_wav_path)
            pygame.mixer.music.play()
        
        # Record start time immediately, then start music
        music_start_time = time.time()
        threading.Thread(target=play_song, daemon=True).start()
        
        # Account for pygame/audio system latency - start IR signals slightly early
        print(f"Music starting, compensating for {self.latency_compensation}s audio latency...")

        colours_for_each_beat = song.get_colours_for_each_beat()
        for index, beat_time in enumerate(beats):
            colour_ir_code = colours_for_each_beat.get(index + 1, None)  # Beats are 1-indexed in the mapping

            # Calculate when this beat should occur relative to music start (with latency compensation)
            target_time = music_start_time + beat_time - self.latency_compensation
            current_time = time.time()
            wait_time = target_time - current_time
            
            if wait_time > 0:
                time.sleep(wait_time)

            print(f"At {beat_time:.2f}s: Beat {index+1}")
            try:
                if colour_ir_code:
                    self.broadlink_client.send_ir_signal(colour_ir_code)
            except Exception as e:
                print(f"Skipping code: {e}")

        print("✅ Done! Light show synced to music.")