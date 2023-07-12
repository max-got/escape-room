# Anleitung

Das ist die Anleitung für das Rätsel Drehschalter.

## 1. Vorbereitung

Das Rätsel verwendet die Sensoren [KY-004 (Taster)](https://sensorkit.joy-it.net/de/sensors/ky-004) und [KY-040 (Kodierter Drehschalter)](https://sensorkit.joy-it.net/de/sensors/ky-040).

Damit die Sensoren verwendet werden können, müssen die folgenden Schritte durchgeführt werden:

1. Die Sensoren müssen an den Raspberry Pi angeschlossen werden. Dazu müssen die Sensoren an die GPIO-Pins angeschlossen werden. Die genaue Pin-Belegung ist in der [Pin-Belegung](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html) zu finden. Das Schema für die Sensoren ist in der folgenden Tabelle zu finden:

**_KY-004_Taster_**

| Raspberry Pi     | Sensor |
| ---------------- | ------ |
| GPIO 26 [Pin 37] | Signal |
| 3,3V [Pin 1]     | +V     |
| GND [Pin 9]      | GND    |

**_KY-040_Kodierter_Drehschalter_** 

| Raspberry Pi     | Sensor |
| ---------------- | ------ |
| GPIO 27 [Pin 13] | Signal |
| GPIO 22 [Pin 15] | Signal |
| 3,3V [Pin 1]     | +V     |
| GND [Pin 20]     | GND    |

Die Sensoren können auch an andere Pins angeschlossen werden. In diesem Fall müssen die Pins in der Konfiguration der `aufgabe1.py`angepasst werden.

## Code

Die Datei `aufgabe1.py` enthält eine Funktion, welche über die main-Datei/Funktion aufgerufen wird. Nach erfolgreichem Starten der Funktion `aufgabe1(counter)`, wobei `counter` mit 1 initialisiert wird, wird die erste Aufgabenstellung des Quizes angezeigt. Nun kann durch Drehen am Drehschalter zwischen den möglichen Antworten ausgewählt werden. Durch das Drehen wird in einem callback eine Funktion ausgeführt, die durch die möglichen Antworten des `q_and_a` Arrays iteriert.  

```python
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
```

## Rätsel

Das Rätsel besteht darin, die richtigen Antworten zu den jeweils im Terminal gestellten Fragen einzugeben. Die Eingabe der Antwortmöglichkeiten erfolgt durch Drehen am Drehschalter. Durch Betätigen des Tasters (Drücken des Knopfes), wird die zuletzt ausgewählte Antwort mit der korrekten Antwort abgeglichen. Ist die Antwort richtig, wird die nächste Frage ausgegeben. Ist die Antwort falsch, wird die Frage erneut gestellt. Dem Array `q_and_a` können die Fragen, Antwortmöglichkeiten und die korrekte Antwort entnommen werden. Zuerst wird Aufgabe 1 gestellt, zum Schluss Aufgabe 4. Ist Aufgabe 4 richtig gelöst, wird Aufgabe 5 mit einer Nachricht ausgegeben. 

## Lösung

Je nach Frage stehen die Lösungen im Array `q_and_a` zur Verfügung, wie in diesem Beispiel:

```python
    q_and_a = {
		1: {
		"frage" :"Wie lautet in Python der Befehl, um einen Text oder eine Variable auf der Konsole auszugeben?",
		"antworten": ["return", "print", "giveback", "console.log", "res.send"],
		"correct": "print"
		},
		#weiterer Code
```