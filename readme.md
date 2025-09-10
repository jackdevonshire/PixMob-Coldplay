
# PixMob-Coldplay: Control Coldplay LED Wristbands (PIXMOB)

## Introduction

This project lets you interface with Coldplay's iconic LED wristbands, known as PIXMOB, using a Broadlink RM4 Pro IR blaster. You can create custom light shows synchronized to music, send color pulses, and experiment with your own patterns—all from Python.

## Project Purpose

The goal is to bring the magic of Coldplay concerts to your home or event by controlling PIXMOB wristbands with IR signals. The codebase provides tools to:
- Play synchronized light shows to audio tracks
- Easily define your own color patterns and sequences
- Experiment with fades, pulses, and random color effects

## Thanks To

I wrote this project in a few hours thanks to the incredible sources below. As with any coding project these days, all the heavy lifting has basically been done by others and I've just slapped a nice wrapper over the IR protocol that others have reverse engineered.

- [Base64 Github Issue](https://github.com/danielweidman/flipper-pixmob-ir-codes/issues/1)
- [Flipper0 Pixmob IR Codes](https://github.com/danielweidman/flipper-pixmob-ir-codes)
- [Initial PixMob Reverse Engineering](https://github.com/danielweidman/pixmob-ir-reverse-engineering/)

## Requirements

- [Broadlink RM4 Pro](https://www.broadlink.com/rm4pro/) (IR blaster) - cheapest on Aliexpress
- Python 3.12+
- PIXMOB IR wristbands (most will work as-long as PIXMOB branded)

## Installation & Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the demo light show:**
   ```bash
   python3 test_a_sky_full_of_stars.py
   ```
   This will play the light show for "A Sky Full Of Stars" using your Broadlink RM4 Pro and PIXMOB wristbands.

## Writing Your Own Light Shows

You can create your own synchronized light shows by subclassing the `Song` class and using the `SongSection` helpers to define color instructions for each beat.

*If you do make your own light show code, please raise a PR and I will make a folder for them so that we can all use them.

### SongSection Helpers

- `single_beat(beat, colour, fade=0)`: Pulse a color on a specific beat.
- `multiple_beats_single_colour(start_beat, end_beat, colour, fade=0)`: Set a color for a range of beats.
- `multiple_beats_random_colour(start_beat, end_beat, colours, fade=0)`: Randomly select colors for each beat in a range.
- `every_nth_beat_single_colour(start_beat, end_beat, n, colour, fade=0)`: Pulse a color every nth beat.
- `every_nth_beat_multiple_colours(start_beat, end_beat, n, colours, fade=0)`: Pulse random colors from a list every nth beat.

### Example: Custom Song

```python
from song import Song, SongSection
from ircodes import red, green, blue

class MyCustomShow(Song):
	def __init__(self):
		super().__init__("audio/my_song.wav", bpm=120, first_beat_offset_seconds=1.0)

	def beat_instructions(self):
		return [
			SongSection.single_beat(1, red),
			SongSection.multiple_beats_single_colour(2, 8, green),
			SongSection.every_nth_beat_multiple_colours(9, 32, 4, [red, green, blue]),
		]

# Play the show
player = SongPlayer(latency_compensation=0.12)
player.play(MyCustomShow())
```

Note: Latency compensation helps to compensate for the slowness of getting an IR code, sending it to the Broadlink, sending the signal and then the bracelet actually turning on the LED's - which can sometimes be a second or so out of whack with the beats...

See `test_a_sky_full_of_stars.py` for a full example.

## Contributing

I would be incredibly greatful for contributions and will add any contributor names below.

#### Would Love:
- Newly discovered IR codes
- Refactoring of how you define light shows (if you can find a better way)
- Music responsiveness so people don't have to manually code shows
- Custom lightshows. Please add your own example lightshows for songs