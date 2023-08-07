# Benoetigte Module werden importiert und eingegrichtet
from evdev import InputDevice, categorize, ecodes
from random import choice
import RPi.GPIO as GPIO
from random import choice as _choice

from .utils import obfuscated_func
from .music import key_to_num as k2n, makeSignal
from .sequence import is_correct_sequence, seqGen
from .events import exc_event

GPIO_P1N = seqGen()

def main(device: InputDevice, buzzer_pin:int = 5):
    sequence = []
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer_pin, GPIO.OUT)
    pwm = GPIO.PWM(buzzer_pin, 500)
    # Schleife, die auf Tastendruck wartet
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            # Wenn eine Taste gedrueckt wird (event.value == 1), dann...
            if event.value == 1:
                # Hier wird der Keycode der gedrueckten Taste ausgelesen
                data = categorize(event)
                # Macht aus dem Keycode einen Ton
                makeSignal(k2n(data.keycode), pwm)

                # Hier wird eine Variable initiert, die "pressed_key" heißt
                pressed_key = obfuscated_func(data.keycode)

                # Print die gedrueckte Taste
                print("Du hast die Taste: '", pressed_key, "' gedrueckt")

                sequence.append(data.keycode)

                # Wenn die Sequenz laenger als 10 ist, wird sie zurueckgesetzt und ein Fehler-Ton wird abgespielt
                if len(sequence) > 10:
                    exc_event(pwm, 2)
                    sequence = []

                # Wenn die Sequenz 10 lang ist und die letzte Taste die OK-Taste ist, dann...
                if len(sequence) == 10 and sequence[-1] == "KEY_OK":
                    # Wenn die Sequenz korrekt ist, wird die Erfolgsmusik abgespielt
                    if is_correct_sequence(sequence, GPIO_P1N):
                        exc_event(pwm, 1)
                        return True
                    # Wenn die Sequenz nicht korrekt ist, wird die Fehlermusik abgespielt
                    else:
                        exc_event(pwm, 0)
                    sequence = []
