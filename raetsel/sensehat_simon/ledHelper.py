import time
from .symbols import checkmark, x
from sense_hat import SenseHat

class LEDHelper:
    def __init__(self, sense: SenseHat):
        if type(sense) != SenseHat:
            raise TypeError("sense must be of type SenseHat")
        self.sense = sense
    def clear(self):
        self.sense.clear(0, 0, 0)
    def show_letter(self, letter, sec=2):
        """
        Display a letter on the LED matrix.
        """
        self.sense.show_letter(letter)
        time.sleep(sec)
        self.sense.clear(0, 0, 0)
    def show_lvl(self, level, sec=2):
        """
        Display the level on the LED matrix.
        """
        self.sense.show_message(str(level))
        time.sleep(sec)
        self.sense.clear(0, 0, 0)
    def show_sequence(self, sec: float, seq: list) -> None:
        """
        Display a sequence of symbols on the LED matrix.
        :param time: The time to display each symbol.
        :param seq: The sequence of symbols to display.
        """
        for i in range(0, len(seq)):
            self.sense.clear(255, 255, 255)
            time.sleep(sec/2)
            self.sense.set_pixels(seq[i])
            time.sleep(sec)
            self.sense.clear(0, 0, 0)
    def won(self, level):
        """
        Display a green and light green color on the LED matrix + a check mark.
        Indicates a successful sequence.
        """
        self.sense.clear(0, 255, 0)
        time.sleep(0.5)
        self.sense.clear(0, 0, 0)
        time.sleep(0.5)
        self.sense.clear(0, 255, 0)
        time.sleep(0.5)
        self.sense.clear(0, 0, 0)
        time.sleep(0.5)
        self.sense.clear(0, 255, 0)
        time.sleep(0.5)
        self.sense.clear(0, 0, 0)
        time.sleep(0.5)
        self.sense.set_pixels(checkmark)
        time.sleep(1)
        self.show_lvl(level)
        self.sense.clear(0, 0, 0)
    def loose(self):
        """
        Display a red and light red color on the LED matrix + an X.
        Indicates a failed sequence.
        """
        self.sense.clear(255, 0, 0)
        time.sleep(0.5)
        self.sense.clear(0, 0, 0)
        time.sleep(0.5)
        self.sense.clear(255, 0, 0)
        time.sleep(0.5)
        self.sense.clear(0, 0, 0)
        time.sleep(0.5)
        self.sense.clear(255, 0, 0)
        time.sleep(0.5)
        self.sense.clear(0, 0, 0)
        time.sleep(0.5)
        self.sense.set_pixels(x)
        time.sleep(1)
        self.sense.clear(0, 0, 0)
    def success(self):
        """
        Display a short green color on the LED matrix.
        """
        self.sense.clear(0, 255, 0)
        time.sleep(0.2)
        self.sense.clear(0, 0, 0)
    def failure(self):
        """
        Display a short red color on the LED matrix.
        """
        self.sense.clear(255, 0, 0)
        time.sleep(0.2)
        self.sense.clear(0, 0, 0)