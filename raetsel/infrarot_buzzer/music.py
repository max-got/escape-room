from time import sleep as _sleep
from random import randint as _randint

from .utils import int_check as _int_check

tooLong_music = {
    'melody': [262, 294, 262, 294, 262],
    'duration': 0.2,
    'pause': 0.1,
}


fail_music = {
    'melody': [392, 330, 294, 262],
    'duration': 0.3,
    'pause': 0.1,
}

success_music = {
    'melody': [
        392, 440, 494, 523, 587, 659, 587, 523, 494, 440,
        392, 392, 440, 440, 494, 494, 523, 523, 587, 587,
        659, 659, 587, 523, 494, 440, 392, 392, 440, 440,
        494, 494, 523, 523, 587, 587, 659, 587, 523, 494,
        440, 392, 392, 440, 440, 494, 494, 523, 523, 587,
        587, 659, 659, 587, 523
    ],
    'duration': 0.1,
    'pause': 0.05,
}


def makeSignal(num: int, pwm) -> None:
    """Gibt einen Ton aus, der die Frequenz der Zahl hat.
    2 -> 200Hz,
    3 -> 300Hz
    sleep(0.5) -> 500ms Pause
    """
    freq = num * 100
    pwm.ChangeFrequency(freq)
    pwm.start(50)
    _sleep(0.5)
    pwm.stop()

def play_music(melody, duration, pause, pwm) -> None:
    """Spielt eine Melodie ab.
    melody: Liste von Frequenzen
    duration: Dauer eines Tons
    pause: Pause zwischen den Tönen
    """
    for freq in melody:
        pwm.ChangeFrequency(freq)
        pwm.start(50)
        _sleep(duration)
        pwm.stop()
        _sleep(pause)

#Nimmt den letzten Buchstaben des Strings und gibt die Frequenz zurück 
#Falls der letzte Buchstabe keine Zahl ist, wird eine zufällige Zahl zwischen 1 und 4 zurückgegeben
def key_to_num(string : str) -> int: 
    """Wandelt den letzten Buchstaben des Strings in eine Zahl um.
    "KEY_NUMERIC_1": 1,
    "KEY_NUMERIC_2": 2,...
    Wenn der letzte Buchstabe des Strings keine Zahl ist, wird eine zufällige Zahl zwischen 1 und 4 zurückgegeben
    """
    if(_int_check(string[-1])):
        num = int(string[-1]) + 1
    else:
        num = _randint(1, 4)
    return num

def play_tooLong_music(pwm) -> None:
    """Spielt die Melodie für zu lange Eingaben ab."""
    play_music(melody =tooLong_music['melody'], duration=tooLong_music['duration'], pause=tooLong_music['pause'], pwm = pwm)

def play_fail_music(pwm) -> None:
    """Spielt die Melodie für falsche Eingaben ab."""
    play_music(melody =fail_music['melody'], duration=fail_music['duration'], pause=fail_music['pause'], pwm = pwm)

def play_success_music(pwm) -> None:
    """Spielt die Melodie für richtige Eingaben ab."""
    play_music(melody =success_music['melody'], duration =success_music['duration'], pause=success_music['pause'], pwm=pwm)
