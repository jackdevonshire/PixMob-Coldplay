from ircodes import red, green, light_green, yellow_green, blue, light_blue, magenta, yellow, pink, orange, white, turquoise
from song import Song, SongSection
from song_player import SongPlayer

class A_Sky_Full_Of_Stars(Song):
    def __init__(self):
        super().__init__("audio/a_sky_full_of_stars.wav", bpm=125, first_beat_offset_seconds=1.2)

    def beat_instructions(self):
        return [
            SongSection.single_beat(1, red), # First beat - TODO, there is a problem with beat indexing
            SongSection.every_nth_beat_single_colour(0, 32, 4, red), # Intro
            SongSection.multiple_beats_single_colour(64, 200, white), # Verse
        ]

if __name__ == "__main__":
    song = A_Sky_Full_Of_Stars()
    player = SongPlayer(latency_compensation=0.12)  # Adjust latency compensation as needed
    player.play(song)