import RPi.GPIO as GPIO
import time
import os

i = 0

def printResultDrehschalter(counter: int, q_and_a):   # dict[int, dict[str, any]]) -> None:
	"""return print value
	
	Die Funktion iteriert durch Array-Elemente des uebergebenen Dictionaries
	und gibt diese ueber die print-Funktion auf dem Terminal aus.
	"""
	Drehschalter_CLK_PIN = 27
	Drehschalter_DT_PIN = 22
	GPIO.setup(Drehschalter_CLK_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(Drehschalter_DT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	global i
	if GPIO.input(Drehschalter_CLK_PIN) == GPIO.input(Drehschalter_DT_PIN): #-1 Richtung zurück
		if i == 0:
			i = len(q_and_a[counter]["antworten"]) - 1
		else: i = i - 1
	else: #+1 Richtung vorwärts
		if i == len(q_and_a[counter]["antworten"]) - 1:
			i = 0
		else: i += 1
	print(q_and_a[counter]["antworten"][i])


def aufgabe1(counter: int) -> int:
	"""return int
	
	Wenn ein Event des Drehschalters detektiert wird, wird ein bestimmtes Element des Dictionaries mit der Counter-Variable
	und der Iterator-Variable an die Funktion printResultDrehschalter uebergeben. 
	Wenn ein Event des Knopfes detektiert wird, wird ueberprueft, ob die Eingabe mit dem richtigen Wert uebereinstimmt.
	"""
	global i
	GPIO.setmode(GPIO.BCM)
	Drehschalter_CLK_PIN = 27
	Drehschalter_DT_PIN = 22
	Knopf_PIN = 26
	GPIO.setup(Drehschalter_CLK_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(Drehschalter_DT_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(Knopf_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	q_and_a = {
		1: {
		"frage" :"Wie lautet in Python der Befehl, um einen Text oder eine Variable auf der Konsole auszugeben?",
		"antworten": ["return", "print", "giveback", "console.log", "res.send"],
		"correct": "print"
		},
		2: {
			"frage" :"Aus wie vielen Zeichen besteht das Hexadezimalalphabet?",
			"antworten" : [2, 4, 13, 9, 16, 11],
			"correct" : 16
		},
		3: {
			"frage" :"Mit welchem Befehl wird eine Funktion mit der Variable 'inputValue' aufgerufen?",
			"antworten" : ["define funktion(inputValue)", "print inputValue", "funktion(inputValue)", "console funktion(inputValue)", "funktion = inputValue"],
			"correct" : "funktion(inputValue)"
		},
		4: {
			"frage" :"Mit welchem Befehl wird geprueft, ob eine Variable einem bestimmten Wert gleicht?",
			"antworten" : ["a != 5", "a is 5", "a = 5", "a and 5", "a == 5"],
			"correct" : "a == 5"
		},
		5: {
			"frage" :"Herzlichen Glueckwunsch, du hast alle Fragen richtig beantwortet.",
			"antworten" : "Die Zahl fuer den Loesungscode lautet 9.",
			"correct" : ""
		}
	}

	print(q_and_a[counter]["frage"])
	GPIO.add_event_detect(Drehschalter_CLK_PIN, GPIO.BOTH, callback=lambda y: printResultDrehschalter(counter, q_and_a), bouncetime=50)
	GPIO.add_event_detect(Knopf_PIN, GPIO.FALLING, bouncetime=100)
	while True:
		if GPIO.event_detected(Knopf_PIN):
			#print("pressed")
			if q_and_a[counter]["antworten"][i] == q_and_a[counter]["correct"]:
				os.system('clear')
				print("Du hast die richtige Antwort ausgewaehlt!")
				counter += 1
				if counter == 5:
					print(q_and_a[counter]["frage"])
					return True
				else:
					print(q_and_a[counter]["frage"])
			else:
				os.system('clear')
				print("Leider falsch, versuche ein anderes Ergebnis.")
				print(q_and_a[counter]["frage"])

#aufgabe1(1)