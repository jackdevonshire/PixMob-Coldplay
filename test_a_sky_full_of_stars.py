from ircodes import red, green, light_green, yellow_green, blue, light_blue, magenta, yellow, pink, orange, white, turquoise
from song import Song, SongSection
from song_player import SongPlayer

class A_Sky_Full_Of_Stars(Song):
    def __init__(self):
        super().__init__("audio/a_sky_full_of_stars.wav", bpm=125, first_beat_offset_seconds=1.2)

    def beat_instructions(self):
            return [
                # First beat
                SongSection.single_beat(1, magenta, fade=6),
                # Intro
                SongSection.every_nth_beat_multiple_colours(0, 32, 4, [blue, light_blue], fade=6),
                # Vocals and build up
                SongSection.every_nth_beat_multiple_colours(33, 63, 2, [pink, light_blue], fade=3),
                # More vocal and build up
                SongSection.every_nth_beat_multiple_colours(64, 95, 2, [turquoise, orange], fade=6),
                # Big beat at 96, magenta pulse
                SongSection.single_beat(96, magenta, fade=0),
                # Continued build up
                SongSection.every_nth_beat_multiple_colours(97, 158, 2, [orange, yellow], fade=6),
                # Chorus 1: explode with all colours, fade 0 (shortest burst)
                SongSection.multiple_beats_single_colour(160, 163, magenta, fade=0), 
                SongSection.multiple_beats_single_colour(163, 167, white, fade=0), 
                SongSection.multiple_beats_random_colour(168, 208, [red, green, light_green, yellow_green, blue, light_blue, magenta, yellow, pink, orange, white, turquoise], fade=0),
                # Chorus stops at 208, soft section begins
                SongSection.every_nth_beat_multiple_colours(209, 240, 4, [blue, light_blue], fade=6),
                # "cause you get lighter the more it gets dark" section starts at 241
                SongSection.every_nth_beat_multiple_colours(241, 255, 2, [pink, turquoise], fade=4),
                # Another beat starts at 256
                SongSection.single_beat(256, yellow, fade=2),
                SongSection.every_nth_beat_multiple_colours(257, 271, 2, [yellow, orange], fade=3),
                # Big beat at 272 - "i don't care"
                SongSection.single_beat(272, magenta, fade=0),
                SongSection.multiple_beats_single_colour(273, 287, pink, fade=2),
                # Another big beat at 288 - "i don't care if you do"
                SongSection.single_beat(288, white, fade=0),
                SongSection.multiple_beats_single_colour(289, 305, light_blue, fade=3),
                # Beat 306 - "cause in a sky, in a sky full of stars"
                SongSection.multiple_beats_random_colour(306, 319, [blue, light_blue, turquoise], fade=4),
                # Beat 320 - "i think i see you"
                SongSection.single_beat(320, pink, fade=2),
                SongSection.every_nth_beat_multiple_colours(321, 335, 2, [pink, yellow], fade=5),
                # Build up starts at 336
                SongSection.every_nth_beat_multiple_colours(336, 343, 1, [orange, yellow], fade=2),
                # "Bam bam" at 344
                SongSection.single_beat(344, magenta, fade=0),
                SongSection.single_beat(348, white, fade=0),
                # Chorus 2 starts at 352
                SongSection.multiple_beats_random_colour(352, 367, [red, green, light_green, yellow_green, blue, light_blue, magenta, yellow, pink, orange, white, turquoise], fade=0),
                # Big beat at 368, continued chorus
                SongSection.single_beat(368, magenta, fade=0),
                SongSection.multiple_beats_random_colour(369, 385, [red, blue, yellow, pink, orange, white], fade=0),
                # Melody changes at 386, more instrumental but still chorus
                SongSection.multiple_beats_random_colour(386, 407, [light_blue, turquoise, pink, white], fade=1),
                # "Oooh ooh oh" at 408
                SongSection.every_nth_beat_multiple_colours(408, 415, 2, [yellow, orange], fade=3),
                # Beat pattern changes at 416
                SongSection.every_nth_beat_single_colour(416, 431, 1, white, fade=0),
                # Another minor change to beat pattern at 432
                SongSection.every_nth_beat_multiple_colours(432, 445, 2, [magenta, blue], fade=1),
                # Still energetic at 446 - "cause you're a sky full of stars"
                SongSection.multiple_beats_random_colour(446, 495, [red, green, light_green, yellow_green, blue, light_blue, magenta, yellow, pink, orange, white, turquoise], fade=0),
                # Wind down to outro at 496
                SongSection.every_nth_beat_multiple_colours(496, 515, 4, [pink, light_blue], fade=5),
                # Fade out at 516
                SongSection.every_nth_beat_single_colour(516, 545, 8, blue, fade=6),
                # End at 546
                SongSection.single_beat(546, white, fade=6),
            ]

if __name__ == "__main__":
    song = A_Sky_Full_Of_Stars()
    player = SongPlayer(latency_compensation=0.12)  # Adjust latency compensation as needed
    player.play(song)

"""

fades bit reakky natching the beat





"""