from ircodes import red, green, light_green, yellow_green, blue, light_blue, magenta, yellow, pink, orange, white, turquoise
from song import Song, SongSection
from song_player import SongPlayer

class A_Sky_Full_Of_Stars(Song):
    def __init__(self):
        super().__init__("audio/a_sky_full_of_stars.wav", bpm=125, first_beat_offset_seconds=1.2)

    def beat_instructions(self):
            return [
                # Dramatic first beat, magenta pulse
                SongSection.single_beat(1, magenta, fade=0),

                # Intro: gentle blue and light_blue pulses, fade 2
                SongSection.every_nth_beat_multiple_colours(2, 32, 2, [blue, light_blue], fade=2),

                # Build-up: rainbow sweep, fade 3
                SongSection.every_nth_beat_multiple_colours(33, 63, 4, [red, orange, yellow, green, turquoise, blue, magenta, pink, white], fade=3),

                # Verse: peaceful white, long fade
                SongSection.multiple_beats_single_colour(64, 159, white, fade=6),
                # Verse: turquoise accents, fade 4
                SongSection.every_nth_beat_single_colour(72, 159, 8, turquoise, fade=4),

                # Big beat at 96, magenta pulse
                SongSection.single_beat(96, magenta, fade=0),

                # Chorus 1: explode with all colours, fade 0 (shortest burst)
                SongSection.multiple_beats_random_colour(159, 210, [red, green, light_green, yellow_green, blue, light_blue, magenta, yellow, pink, orange, white, turquoise], fade=0),

                # Winds back down: soft pink and light_green, fade 5
                SongSection.every_nth_beat_multiple_colours(211, 271, 4, [pink, light_green], fade=5),

                # Big beat at 272, white pulse
                SongSection.single_beat(272, white, fade=0),

                # Build up: turquoise and blue, fade 3
                SongSection.every_nth_beat_multiple_colours(320, 334, 2, [turquoise, blue], fade=3),

                # More build up: magenta and yellow, fade 2
                SongSection.every_nth_beat_multiple_colours(335, 351, 2, [magenta, yellow], fade=2),

                # Big beat into chorus again, orange pulse
                SongSection.single_beat(352, orange, fade=0),

                # Chorus 2: different random pattern, fade 0
                SongSection.multiple_beats_random_colour(384, 415, [red, green, yellow, blue, magenta, pink, orange, turquoise, white], fade=0),

                # New pattern: alternating green and light_blue, fade 4
                SongSection.every_nth_beat_multiple_colours(416, 449, 3, [green, light_blue], fade=4),

                # More vocals for chorus: peaceful white, fade 6
                SongSection.multiple_beats_single_colour(450, 480, white, fade=6),
            ]

if __name__ == "__main__":
    song = A_Sky_Full_Of_Stars()
    player = SongPlayer(latency_compensation=0.12)  # Adjust latency compensation as needed
    player.play(song)