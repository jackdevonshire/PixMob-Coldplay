from ircodes import red, green, light_green, yellow_green, blue, light_blue, magenta, yellow, pink, orange, white, turquoise
import random
from enum import Enum
"""
    This class is used to help define a song, 
    and what colours on the wristband should be playing for
    each beat of the song.
"""
class SongInstruction():
    def __init__(self, beat, colour_ir_code):
        self.beat = beat
        self.colour_ir_code = colour_ir_code

class SongSection():
    def __init__(self, start_beat=0, end_beat=0, colours=None):
        self.start_beat = start_beat
        self.end_beat = end_beat
        self.colours = colours if colours is not None else []

    @staticmethod
    def single_beat(beat, colour, fade=0):
        return [SongInstruction(beat, colour.get_ir_signal(fade))]

    @staticmethod
    def multiple_beats_single_colour(start_beat, end_beat, colour, fade=0):
        return [SongInstruction(beat, colour.get_ir_signal(fade)) for beat in range(start_beat, end_beat + 1)]

    @staticmethod
    def multiple_beats_random_colour(start_beat, end_beat, colours, fade=0):
        instructions = []
        for beat in range(start_beat, end_beat + 1):
            colour = random.choice(colours)
            instructions.append(SongInstruction(beat, colour.get_ir_signal(fade)))
        return instructions

    @staticmethod
    def every_nth_beat_single_colour(start_beat, end_beat, n, colour, fade=0):
        instructions = []
        beat = start_beat
        while beat <= end_beat:
            instructions.append(SongInstruction(beat, colour.get_ir_signal(fade)))
            beat += n
        return instructions
    
    @staticmethod
    def every_nth_beat_multiple_colours(start_beat, end_beat, n, colours, fade=0):
        instructions = []
        beat = start_beat
        while beat <= end_beat:
            colour = random.choice(colours)
            instructions.append(SongInstruction(beat, colour.get_ir_signal(fade)))
            beat += n
        return instructions

class Song:
    def __init__(self, audio_wav_path, bpm, first_beat_offset_seconds=0):
        self.audio_wav_path = audio_wav_path
        self.bpm = bpm
        self.beat_interval = 60.0 / bpm  # Time between beats in seconds
        self.first_beat_offset_seconds = first_beat_offset_seconds

    def get_colours_for_each_beat(self):
        """
            Returns a list of colours signals to play for each beat in the song
        """
        beats_colours = {} # Beat to colour
        
        for section in self.beat_instructions():
            for instruction in section:
                beats_colours[instruction.beat] = instruction.colour_ir_code
        
        return beats_colours

    def beat_instructions(self):
        """
            Returns colours to play at each beat
        """
        return [
            SongSection.single_beat(1, red),
            SongSection.multiple_beats_single_colour(2, 8, green),
            SongSection.multiple_beats_single_colour(9, 16, light_green),
            SongSection.multiple_beats_random_colour(17, 32, [yellow_green, yellow, orange, pink, light_green, light_blue, turquoise, white]),
        ]