# Anleitung

Das ist die Anleitung für das Rätsel Infrarot-Abstandsdetektor.

## 1. Vorbereitung

Das Rätsel verwendet den Sensor [KY-032 (Hindernis-Detektor)](https://sensorkit.joy-it.net/de/sensors/ky-032) und eine grüne und eine rote LED, die über Widerstände angeschlossen sind.

Damit die Sensoren verwendet werden können, müssen die folgenden Schritte durchgeführt werden:

1. Die Sensoren müssen an den Raspberry Pi angeschlossen werden. Dazu müssen die Sensoren an die GPIO-Pins angeschlossen werden. Die genaue Pin-Belegung ist in der [Pin-Belegung](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html) zu finden. Das Schema für die Sensoren ist in der folgenden Tabelle zu finden:

**_KY-032_Hindernis-Detektor_**

| Raspberry Pi     | Sensor |
| ---------------- | ------ |
|       --         | Enable |
| GPIO 4 [Pin 7]   | Signal |
| 3,3V [Pin 1]     | +V     |
| GND [Pin 6]      | GND    |

**_Grüne_LED_** 

| Raspberry Pi     | Sensor |
| ---------------- | ------ |
| GPIO 18 [Pin 12] | Signal |
| GND [Pin 9]     | GND    |

**_Rote_LED_** 

| Raspberry Pi     | Sensor |
| ---------------- | ------ |
| GPIO 17 [Pin 11] | Signal |
| GND [Pin 14]     | GND    |

Die Sensoren können auch an andere Pins angeschlossen werden. In diesem Fall müssen die Pins in der Konfiguration der `aufgabe2.py`angepasst werden.

## Code

Die Datei `aufgabe2.py` enthält eine Funktion, welche über die main-Datei/Funktion aufgerufen wird. Nach erfolgreichem Starten der Funktion `aufgabe2()` müsste die die grüne LED in kurzen sich wiederholenden Abständen blinken.

Je nachdem, ob der Infrarot-Abstandssensor ein Hindernis detektiert, wird die entsprechende LED zum Leuchten gebracht. Wird beispielsweise kein Hindernis erkannt, ist die erste Bedingung erfüllt `if GPIO.input(Lichtschranke_PIN) == True`. 

```python
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
```

## Rätsel

Das Rätsel besteht darin, die richtige Sequenz von Unterbrechungen im Infrarotsensor zu ermitteln. Mittels `detection_array.append()` wird je nachdem, ob ein Hindernis erkannt bzw. nicht erkannt wurde, eine 0 (kein Hindernis erkannt) oder eine 1 (Hindernis erkannt) der Sequenz `detection_array` hinzugefügt. 
Alle 2 Sekunden wird ein Wert gemessen und entsprechend in das `detection_array` eingetragen. Ist das Infrarot-Signal nicht unterbrochen, erscheint im Terminal „Kein Hindernis“, der Liste wird die Zahl 0 angefügt und die grüne LED blinkt. Wird das Signal unterbrochen (bspw. durch nahes Heranhalten des Fingers oder eines Gegenstandes an das Signal), erscheint beim nächsten Messen „Hindernis“ und der Liste wird die Zahl 1 angefügt. Statt der grünen LED leuchtet nun die rote LED. Hinweis: das Infrarot-Signal muss so lange unterbrochen werden, bis der nächste Messwert erhoben wird, also maximal 2 Sekunden.
Ziel ist es die grüne und rote LED abwechselnd leuchten zu lassen – das gelingt, indem das Signal 2 Sekunden unterbrochen wird und dann wieder 2 Sekunden nicht. Dabei wird die Liste im Terminal erzeugt. Die richtige Liste ist somit [0, 1, 0, 1], also grünes Leuchten, rotes Leuchten, grünes Leuchten, rotes Leuchten. 
Sofern die Zahlenkombination der Liste falsch ist, wird die Liste nach 5 Zahlen zurückgesetzt und neu erstellt. Die Teilnehmenden haben also nach 5 Zahlen eine neue Chance durch Unterbrechen des Signals die richtige Liste zu generieren. Wird eine Liste zwei Mal zurückgesetzt erhalten die Teilnehmenden einen ersten Tipp zur Lösung des Rätsels, nach vier Mal Zurücksetzen erhalten sie einen zweiten Tipp. 

## Lösung

Um das Rätsel zu lösen, müssen die Teilnehmenden die Sequenz 0, 1, 0, 1 eingeben, indem sie alle 2 Sekunden ihren Finger auf den Infrarotsensor halten, sodass die LED's abwechselnd grün und rot leuchten.
