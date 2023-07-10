import RPi.GPIO as GPIO
import time
import os

def aufgabe2():
	GPIO.setmode(GPIO.BCM)
	detection_array = []
	info_schedule = 0
	Lichtschranke_PIN = 4
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(17, GPIO.OUT)
	GPIO.setup(Lichtschranke_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	while True:
		if GPIO.input(Lichtschranke_PIN) == True:
			print("Kein Hindernis")
			GPIO.output(18, True)
			detection_array.append(0)
			print(detection_array)
			time.sleep(1)
			GPIO.output(18, False)
			time.sleep(1)
		else:
			print("Hindernis")
			GPIO.output(17, True)
			detection_array.append(1)
			print(detection_array)
			time.sleep(1)
			GPIO.output(17, False)
			time.sleep(1)
		time.sleep(2)
		if detection_array == [0, 1, 0, 1]:
			print("Richtig, du hast das Raetsel geloest!")
			return True
		elif len(detection_array) == 5:
			detection_array = []
			info_schedule += 1
			os.system('clear')
			if info_schedule == 2:
				print("Tipp 1: Durch Unterbrechen des Lichtschranken-Sensors, leuchtet das rote Licht.")
			elif info_schedule == 4:
				print("Tipp 2: Du musst durch das Unterbrechen der Lichtschranke die richtige Reihenfolge von 0en und 1en ermitteln, um das Raetsel zu loesen.")
			elif info_schedule == 5:
				info_schedule = 0
