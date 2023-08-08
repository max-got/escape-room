from drehschalter import aufgabe1
from infrarot_abstand import aufgabe2
from sensehat_simon import escape as simon_escape
from infrarot_buzzer import escape as infrarot_escape
from sensehat_3in1 import sensehat_riddle as aufgabe4
from hand_recognition import escape_ASL as asl
from evdev import InputDevice
import RPi.GPIO as GPIO
from sense_hat import SenseHat
from functools import partial

s = SenseHat()

#kann auch event0, event1, event2, event3 sein
infrarot_sensor = InputDevice("/dev/input/event3")
#buzzer GPIO-PIN 
buzzer_pin = 5

raetsel = 1


def lvl_up(fn, GPIO, level: int) -> True:
	s.show_letter(str(level))
	global raetsel
	print("Momentanes Level " + str(level))
	completed = False
	
	while completed == False:
		completed = fn()
	GPIO.cleanup()
	raetsel = raetsel + 1
	return completed

def start_escape_room():	
		try:
			if raetsel == 1:
				lvl_up(partial(aufgabe1.aufgabe1, 1), GPIO, raetsel) 
			if raetsel == 2:
				lvl_up(partial(aufgabe2.aufgabe2), GPIO, raetsel)
			if raetsel == 3:
				lvl_up(partial(simon_escape.main), GPIO, raetsel) 
			if raetsel == 4:
				lvl_up(partial(aufgabe4.main), GPIO, raetsel) 
			if raetsel == 5:
				s.show_letter("?")
				print("Nimmst du am Workshop teil? j/n")
				x = input("Bitte j oder n eingeben: ")	
				if x == "J" or x == "j":
					lvl_up(partial(asl.main), GPIO, raetsel)
				else:
					return(print("Escape-Room bendet"))
			if raetsel == 6: 
				lvl_up(partial(infrarot_escape.main, device = infrarot_sensor, buzzer_pin = buzzer_pin ), GPIO, raetsel) 
			if raetsel == 7:
				s.clear()
				
		except KeyboardInterrupt:
			GPIO.cleanup()
			s.clear()
			raise Exception("Der Escape Room wurde beendet.")
		except Exception as e:
			print(e)
			GPIO.cleanup()
			s.clear()


 
start_escape_room()
