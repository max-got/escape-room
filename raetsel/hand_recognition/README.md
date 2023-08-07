# Anleitung

Das ist die Anleitung für das Handerkennungsrätsel.

## 1. Vorbereitung

Das Rätsel verwendet die Sensoren [KY-004 (Taster)](https://sensorkit.joy-it.net/de/sensors/ky-004), eine einfache USB Webcam und die LED-Matrix des [Sensehat](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat).

Damit der Sensor verwendet werden kann, müssen die folgenden Schritte durchgeführt werden:

Der Sensor muss an den Raspberry Pi angeschlossen werden. Dazu muss der Sensor an die GPIO-Pins angeschlossen werden. Die genaue Pin-Belegung ist in der [Pin-Belegung](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html) zu finden. Das Schema für den Sensor ist in der folgenden Tabelle zu finden:

**_KY-004_Taster_**

| Raspberry Pi     | Sensor |
| ---------------- | ------ |
| GPIO 26 [Pin 37] | Signal |
| 3,3V [Pin 1]     | +V     |
| GND [Pin 9]      | GND    |

Die Sensoren können auch an andere Pins angeschlossen werden. In diesem Fall müssen die Pins in der Konfiguration der `aufgabe1.py`angepasst werden.

Der Sensehat sollte wie folgt angeschlossen werden:
Benötigt werden 11 Jumper Kabel und der Sensehat

| Raspberry Pin | Sensehat Pin | Type   |
| ------------- | ------------ | ------ |
| 1             | 1            | 3.3V   |
| 2             | 2            | 5V     |
| 6             | 6            | GND    |
| 3             | 3            | GPIO2  |
| 5             | 5            | GPIO3  |
| 16            | 16           | GPIO23 |
| 18            | 18           | GPIO24 |
| 22            | 22           | GPIO25 |
| 24            | 24           | GPIO8  |
| 27            | 27           | GPIO0  |
| 28            | 28           | GPIO1  |

Da das Pinlayout auf dem Sensehat identisch zu dem auf dem Raspberry ist lassen sich die Kabel relativ einfach dem entsprechenden Anschluss zuordnen.

Die Webcam kann einen einfachen USB-Anschluss angeschlossen werden.

## Code

In der `main` werden alle benötigten Variablen initialisiert, darunter verschiedene Farben und Logos für den Sensehat. Die gesamte Logik für die Handerkennung läuft in einer einfachen while True Endlosschleife.

Die Buchstaben werden dabei in der Schleife alle gleich Definiert. Dazu wird eine if-Abfrage genutzt, welche die Position und Ausrichtung der Finger abgleicht. Dazu gibt es ein paar Funktionen, wie `indexDown` und `indexUp`, oder es werden die direkten Koordinaten der erkannten Hand Landmarks verglichen. Die Landmarks können auf dem Bild `hand_landmarks.png` eingesehen werden. Der erkannte Buchstabe wird dann an die Funktion `detected` übergeben.

```python
if indexDown(a) and middleDown(a) and ringDown(a) and pinkyDown(a) and a[4][2:] < a[3][2:] and a[4][1:] > a[0][1:] and a[4][1:] > a[6][1:] and a[4][2:] < a[7][2:]    :
                detected("A", sequence)
```

Die Funktion `detected` zeigt den übergebenen Buchstaben auf dem Sensehat an. Sollte dann der Knopf gedrückt werden, wird der Buchstabe bestätigt. Der Buchstabe läuft dann auf dem Sensehat erneut durch als Feedback, bevor der Wert and die `setSequence`-Funktion weiter gegeben wird.

```python
def detected(text, sequence):
    sense.show_letter(text)
    if GPIO.event_detected(Knopf_PIN):
        sense.show_message(text)
        setSequence(text,sequence)
```

Die `setSequence`-Funktion fügt den bestätigten Buchstaben der Sequenz hinzu. Zusätlich gibt es Abfragen damit die Sequenz nicht länger als 3 Stellen wird.

```python
def setSequence(value, sequence):
    sense.clear()
    if len(sequence) == 0:
        sequence.append(value)
        
    if value != sequence[-1]:
        sequence.append(value)
    
    if len(sequence) > 3:
        sequence.pop(0)
```
In der while-Schleife gibt es zum Ende eine einfache Abfrage der Länge der Sequenz. Sollte diese eine Länge von 3 hat, wird die Funktion `checkSolution` aufgerufen. Sollte diese `True` zurückliefern so ist das Rätsel gelöst und es kann final True an die init zurückgeliefert werden.

```python
if len(sequence) == 3:

                if checkSolution(sequence, logo) == True:
                    return True
```

In `checkSolution` wird die aktuell eingegebene Sequenz mit der Lösung verglichen. Dazu wird die verschlüsselte Lösung entschlüsselt und geschaut ob sich beide gleichen. Sollte dies stimmen so wird das Logo der THB blinkend angezeigt, das Kamerafenster geschlossen und `True` returned.

```python
def checkSolution(solution, logo):
    solution = ''.join(solution)   
    if solution == bytes.fromhex("544842").decode('utf-8'):
        print("Glückwunsch!")
        for i in range(0, 3):
            sense.set_pixels(logo)
            time.sleep(.3)
            sense.clear()
            time.sleep(.3)
        cv2.destroyAllWindows()
        return True
    else:
        return False
```


## Rätsel

In diesem Rätsel können über verschiedene Gesten Buchstaben eingegeben werden. Diese basieren auf dem American Sign Language Alphabet, welches auch auf dem Bild `ASL_Alphabet.png` zu finden ist. Dieses Bild sollte den Teilnehmenden auch zur Verfügung gestellt werden. Die Gesten werden auf dem Sensehat angezeigt und können dann per Knopfdruck bestätigt werden und dem Lösungswort hinzugefügt werden.
Über eine Analyse des Codes sollen die Teilnehmenden herrasufinden welches Lösungswort per Handerkennung eingegeben werden soll. Dazu gibt es einige Funktionen mit Kommentaren die diese Analyse unterstützen soll. In diesen Kommentaren wird zum Beispiel die länge und verschlüsselung der Lösung beschrieben.

## Lösung

Die Lösung ist in der Funktion `checkSolution` zu sehen, sie ist jedoch durch eine hex Codierung verschlüsselt. Entschlüsselt ergibt der String '544842' das Lösungswort 'THB'. Wenn dieses eingegeben wird ist das Rätsel gelöst und das THB-Logo wird auf dem Sensehat angezeigt.