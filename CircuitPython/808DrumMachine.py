import audioio
import touchio
import board
import time

from digitalio import DigitalInOut, Direction

bpm = 120
audioFiles = [
    'bass_hit_c.wav',
    'bd_tek.wav',
    'bd_zome.wav',
    'drum_cowbell.wav',
    'elec_blip2.wav',
    'elec_cymbal.wav',
    'elec_hi_snare.wav'
]

# Enable the speaker
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = True

# Analog audio output
a = audioio.AudioOut(board.A0)

# Enable capacitive touch pads on A1-7
capPins = (board.A1, board.A2, board.A3, board.A4, board.A5, board.A6, board.A7)
touchPad = []
 
for i in range(7):
  touchPad.append(touchio.TouchIn(capPins[i]))

def play_file(filename):
    f = open(filename, "rb")
    wave = audioio.WaveFile(f)
    a.play(wave)
    time.sleep(bpm/960)  # sixteenthNote delay

while True:
    for i in range(7):
        if touchPad[i].value:
            play_file(audioFiles[i])