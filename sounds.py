import numpy as np
import sounddevice as sd
import simpleaudio as sa


RATE = 44100
TONES = {
    'LOW': 200,
    'MEDIUM': 440,
    'HIGH': 700
}
LENGTHS = {
    'SHORT': 0.3,
    'MEDIUM': 0.6,
    'LONG': 1.2
}


def square(freq, linspace):
    a = np.sin(freq * linspace) / 2 + 0.5
    d = np.round(a) - 0.5
    return d * 0.3


def linespace(duration):
    return np.linspace(0, duration * 2 * np.pi, int(duration * RATE))

def draw_sound():
    x = linespace(LENGTHS['SHORT'])
    sound = square(TONES['LOW'], x)

    sd.play(sound, RATE)

def hit_sound():
    x = linespace(LENGTHS["SHORT"])
    sound = square(TONES["MEDIUM"], x)

    sd.play(sound, RATE)


def win_sound():
    short_x = linespace(LENGTHS['SHORT'])
    medium_x = linespace(LENGTHS['LONG'])

    sound1 = square(TONES['HIGH'], short_x)
    sound2 = square(TONES['LOW'], medium_x)

    sound = np.concatenate((sound1, sound2))


    sd.play(sound, RATE)

    
