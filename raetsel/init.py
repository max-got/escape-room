from drehschalter import aufgabe1
from infrarot_abstand import aufgabe2
from sensehat_simon import escape
import RPi.GPIO as GPIO
from sense_hat import SenseHat
import time
from functools import partial

raetsel = 1
s = SenseHat()

lvls = [{"fn": aufgabe1.aufgabe1, "args": 1},
	{"fn": aufgabe2.aufgabe2, "args": ""},
	{"fn": escape.main, "args": ""}
	]
print(lvls[0]["fn"])

def lvl_up(fn, GPIO, level: int) -> True:
	s.show_letter(str(level))
	global raetsel
	print("curr_lvl" + str(level))
	completed = False
	
	while completed == False:
		completed = fn()
	GPIO.cleanup()
	raetsel = raetsel + 1
	return completed
	
def start_escape_room():
	#while True:
	for i in range(0, len(lvls)):
		try:
			lvl_up(partial(lvls[i]["fn"], lvls[i]["args"]), GPIO, raetsel)
		except:
			pass
			#print(i)


start_escape_room()


'''def start_escape_room():	
	while True:
		try:
			if raetsel == 1:
				lvl_up(partial(aufgabe1, 1), GPIO, raetsel) 
			if raetsel == 2:
				lvl_up(partial(aufgabe2), GPIO, raetsel) 
		except KeyboardInterrupt:
			GPIO.cleanup()
		except Exception as e:
			print(e)
			GPIO.cleanup()
'''
