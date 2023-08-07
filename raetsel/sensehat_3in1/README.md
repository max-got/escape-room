# Anleitung

Das ist die Anleitung für das Rätsel Sensehat Sensoren.

## 1. Vorbereitung

Das Rätsel verwendet die eingebauten Sensoren auf dem [Sensehat](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat).

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

## Code

Zu beginn des Programms werden alle nötigen Variablen definiert und gespeichert. 

| Varibalen Name     | Type      | Beschreibung                                                               |
| ----------------   | --------- | -------------------------------------------------------------------------- |
| stickValue         | Integer   | Zufällig generierter Wert (0-8), dient als (Start-)Wert für den Joystick   |
| temp               | Integer   | Aktueller Temperaturwert, über den Humidity-Sensor des Sensehat ausgelesen |
| gyro               | Integer   | Aktuelle Neigung des Sensehat, über Gyro-Sensor des Sensehat ausgelesen    |
| gyroValue          | Integer   | Dient als Wert zur darstellung des Neigung, Standardmäßig auf 2 gesetzt    |
| stickSolved        | Boolean   | Boolean zur Überprüfung ob stickValue dem Lösungswert entspricht           |
| tempSolved         | Boolean   | Boolean zur Überprüfung ob temp um den Wert 2 verringert wurde             |
| gyroSolved         | Boolean   | Boolean zur Überprüfung ob gyroValue dem Lösungswert entspricht            |

```python
def main():
	sense.set_rotation(180)
	sense.clear()
	
	stickValue = random.randint(0,8)
	
	temp = sense.get_temperature()
	tempValue = 5
	print(temp)
	
	sense.set_imu_config(False, True, False)
	gyro = sense.get_gyroscope()
	gyroValue = 2
	print(gyro["roll"])
	
	if stickValue != 5:
		stickSolved = False
	elif stickValue == 5:
		stickSolved = True
	
	tempSolved = False
	
	gyroSolved = False

	setStickBar(stickValue)
	setTempBar(tempValue)
	setGyroBar(gyroValue)
```
Die Funktionen `setStickBar`, `setTempBar` und `setGyroBar` werden mit den initalen Werten aufgerufen. Dadruch werden die entsprechenden Balken auf dem Sensehat dargestellt. Wie genau die Funktionen funktionerne wird in den entsprechenden Unterkapitlen beschrieben.

Der zweiten Teil der `main`-Funktion wird durch eine while-Schleife gebildet. Diese führt so lange aus bis alle Varibalen (`stickSolved`, `tempSolved`, `gyroSolved`) auf `True` gesetzt wurden. Sobald die Variablen `True` entsprechend und die Bedingung der Schleife nicht mehr erfüllen wir außerhalb der Schleife die Funktion `solved` aufgerufen. In dieser Schleife werden die entsprechenden Logiken für die Teilrätsel umgesetzt. Diese werden auch im einzelen in der Unterkapiteln beschrieben. 

```python
while stickSolved == False or tempSolved == False or gyroSolved == False:
```

Die Fuktion `solved` spielt eine kurze Animation ab, welche aus einem 3-maligen blinken der korrekten Lösung besteht. Anschließend wird mit `return True` die abschließenden Rückgabe, und damit die Bestätigung der korrekten Lösung des Rätsels, an die `init` durchgeführt.

```python
def solved():
	for i in range(0,3):
		setStickBar(0)
		setTempBar(0)
		setGyroBar(0)
		time.sleep(.3)
		setStickBar(5)
		setTempBar(3)
		setGyroBar(6)
		time.sleep(.3)
	return True
```

### Joystick

Innerhalb der Schleife in der `main`-Funktion wird über eine Abfrage mithilfe der Funktion `sense.stick.get_events` geschaut ob der Joystick auf dem Sensehat gedrückt wird. Sollte das Event `pressed` detektiert werden wird überprüft in welche Richtung gedrückt wurde. Für unseren Fall sind nur die Events `up` und `down` relevant. Im Fall das der Joystick nach oben gedrückt wird, wird die Variable `stickValue` um 1 erhöht und die Funktion `setStickBar` mit dieser aufgerufen. Wird der Joystick nach unten gedrückt so wird `stickValue` um 1 verringert und `setStickBar` mit dem entsprechenden Wert aufgerufen. Der Returnwert von `setStickBar` wird der Variable `stickSolved` zugeordnet. Da die LED-Matrix auf dem Sensehat eine größe von 8x8 hat wird über einfache if-Abfragen sichergestellt das `stickValue` nicht größer als 8 oder kleiner als 0 wird.

```python
for event in sense.stick.get_events():
			
			# Check if the joystick was pressed
			if event.action == "pressed":
		  
			# Check which direction and update value accordingly to call function to set the pixels
		  
				if event.direction == "up":
					if stickValue < 8:
						stickValue = stickValue + 1
						stickSolved = setStickBar(stickValue)      # Up arrow
				elif event.direction == "down":
					if stickValue > 0:
						stickValue = stickValue - 1
						stickSolved = setStickBar(stickValue)      # Down arrow
```

Die Funktion `setStickBar` sorgt dafür das der aktuelle Wert auf dem Sensehat abgebildet wird. `stick` ist dabei ein Integer welcher beim Aufruf übergeben wird. In der ersten Zeile wird die Funktion `clearBar` ausgeführt. Mit den übergebenen Koordinaten wird dadurch der gesamte Bereich des Balkens für den Joystickwert freigemacht, um den aktualisierten Wert darzustellen. Es folgen zwei geschachtelte for-Schleifen welche über den zuvor freigemachten Bereich iterieren. Die erste Schleife ist dabei für die y-Achse zuständing und läuft bis zu dem übergebenen Wert `stick`. Die zweite Schleife iteriert über die x-Asche. Innerhalb dieser Schleifen befindet sich eine einfache Abfrage ob der übergebene Wert dem gewünschten Lösungswert entspricht. Sollte dies der Fall sein, so wird der Balken über den RGB Wert `(0, 255, 0)` grün dargestellt. Andernfalls wird der Balken entsprechend durch `(255, 0, 0)` in rot visualisiert. Abschließend wird `True` zurückgebenen wenn der `stick` dem Lösungswert entspricht oder eben `False` sollten sie sich nicht gleichen.

```python
def setStickBar(stick):
	clearBar(0, 2)
	for y in range(0,stick):
		for x in range(0,2):
			if stick == 5:
				sense.set_pixel(x, y, (0, 255, 0))
			else:
				sense.set_pixel(x, y, (255, 0, 0))
	if stick == 5:
		return True
	else:
		return False
```

### Temperatur

Für den Temperaturteil des Rätsels wird ständig in der while-Schleife überprüft ob sich die Temperatur um einen ganzen Grad Celsius erhöht oder verringert hat. Sollte einer dieser Fälle eintreten, so wird die neue aktuelle Temperatur über `sense.get_temperature` in der Varibale `temp` gespeichert. Daraufhin funktioniert die Logik genau wie bereits oben beim Joystick. Die Variable `tempValue` wird entsprechend um 1 erhöht oder verringert und mit ihr die Funktion `setTempBar` aufgerufen. Auch hier wird das zurückgebene Ergebniss in `tempSolved` gespeichert. Ebenso gibt es eine einfache Abfrage, sodass der Wert von `tempValue` nicht größer als 8 oder kleiner als 0 wird.

```python
if sense.get_temperature() <= temp-1:
    if tempValue > 0:
        temp = sense.get_temperature()
        tempValue = tempValue - 1
        tempSolved = setTempBar(tempValue)
			
if sense.get_temperature() >= temp+1:
    if tempValue < 8:
        temp = sense.get_temperature()
        tempValue = tempValue + 1
        tempSolved = setTempBar(tempValue)
```

Die `setTempBar`-Funktion ist auch parralel zu der `setStickBar`-Funktion aufgebaut. Zuerst wird die Funktion `clearBar` mit den entsprechenden Koordinaten aufgerufen. Dannach über den Bereich iteriert und der Balken bis zu dem y-Wert den `temp` angibt in Grün oder Rot dargestellt. Genauso wird im Falle des korrekten Werts `True` zurückgegeben, andernfalls `False`.

```python
def setTempBar(temp):
	clearBar(3, 5)
	for y in range(0,temp):
		for x in range(3,5):
			if temp == 3:
				sense.set_pixel(x, y, (0, 255, 0))
			else:
				sense.set_pixel(x, y, (255, 0, 0))
	if temp == 3:
		return True
	else:
		return False
```

### Gyro

Für das Teilrätsel Gyroscope werden in der while-Schleife dauerhaft alle möglichen Szenarien überprüft. Die Abfragen sind dabei identisch aufgebaut, fragen jedoch entsprechend andere Werte ab und rufen die Funktion `setGyroBar` mit dem für das Szenario zutreffenden Wert auf. In der if-Abfrage wird dabei immer geschaut ob die, durch die Funktion `sense.get_gyroscope` ausgelesene, Neigung sich in einem bestimmten Bereich befindet. Welcher Bereich welchem Wert auf der Anzeige entspricht kann aus folgender Tabelle abgelesen werden:

| Neigung     | Wert |                                      
| ----------- | ---- |
| 0 - 20 °    | 4    |
| 20 - 40 °   | 3    |
| 40 - 60 °   | 2    |
| 60 - 80 °   | 1    |
| 80 - 180 °  | 0    |
| 180 - 300 ° | 8    |
| 300 - 320 ° | 7    | 
| 320 - 340 ° | 6    |
| 340 - 360 ° | 5    |

```python
if sense.get_gyroscope()["roll"] < 180 and sense.get_gyroscope()["roll"] > 80:
	gyroSolved = setGyroBar(0)
		
if sense.get_gyroscope()["roll"] < 80 and sense.get_gyroscope()["roll"] > 60:
    gyroSolved = setGyroBar(1)
    
if sense.get_gyroscope()["roll"] < 60 and sense.get_gyroscope()["roll"] > 40:
    gyroSolved = setGyroBar(2)
    
if sense.get_gyroscope()["roll"] < 40 and sense.get_gyroscope()["roll"] > 20:
    gyroSolved = setGyroBar(3)
    
if sense.get_gyroscope()["roll"] < 20 and sense.get_gyroscope()["roll"] > 0:
    gyroSolved = setGyroBar(4)

if sense.get_gyroscope()["roll"] < 360 and sense.get_gyroscope()["roll"] > 340:
    gyroSolved = setGyroBar(5)
    
if sense.get_gyroscope()["roll"] < 340 and sense.get_gyroscope()["roll"] > 320:
    gyroSolved = setGyroBar(6)
    
if sense.get_gyroscope()["roll"] < 320 and sense.get_gyroscope()["roll"] > 300:
    gyroSolved = setGyroBar(7)
    
if sense.get_gyroscope()["roll"] < 300 and sense.get_gyroscope()["roll"] > 280:
    gyroSolved = setGyroBar(8)
    
if sense.get_gyroscope()["roll"] < 280 and sense.get_gyroscope()["roll"] > 180:
    gyroSolved = setGyroBar(8)
```

Die `setGyroBar`-Funktion ist auch parralel zu den Funktionen `setStickBar` und `setTempBar` aufgebaut. Zuerst wird die Funktion `clearBar` mit den entsprechenden Koordinaten aufgerufen. Dannach über den Bereich iteriert und der Balken bis zu dem y-Wert den `gyr0` angibt in Grün oder Rot dargestellt. Genauso wird im Falle des korrekten Werts `True` zurückgegeben, andernfalls `False`.

```python
def setGyroBar(gyro):
	clearBar(6, 8)
	for y in range(0,gyro):
		for x in range(6,8):
			if gyro == 6:
				sense.set_pixel(x, y, (0, 255, 0))
			else:
				sense.set_pixel(x, y, (255, 0, 0))
	if gyro == 6:
		return True
	else:
		return False
```


## Rätsel

Das Rätsel besteht aus 3 Teilen. Jeder Teil nutzt dazu einen anderen Sensor des Sensehat. Bei jedem Sensor ist das Ziel den Wert durch sein handeln in einen entsprechenden, korrekten Bereich  zu bringen. Bei den 3 Sensoren handelt es sich um den Joystick, den Temperatursensor und den eingebauten Gyrosensor. Eine Darstellung der Werte findet auf dem Sensehat in Form von 3 Balkendiagrammen statt. Die Balken werden grundsätzlich in Rot dargestellt. Sobald der Wert korrekt eingestellt ist gibt es ein visuelles Feedback, da der entsprechende Balken daraufhin in Grün erleuchtet. Hauptziel ist es den Nutzer weiter mit dem Sensehat und verschiedenen Sensoren vertraut zu machen.

### Joystick

Bei Start des Programms wird ein zufälliger Wert zwischen 0 und 8 festgelegt. Dieser Wert ist der Startwert, welcher visuell auf dem Sensehat dargestellt wird. Ziel ist es nun herrauszufinden das sich der Wert durch den Joystick verändern lässt und auf welchen Wert der Balken eingestellt werden soll. Dieses Teilrätsel wird auch als erstes vorgesehen, damit die Nutzer sich mit dem Prinzip der Balken und dem Feedback für korrekte Einstellungen vertraut machen können.

### Temperatur

Der Temepraturwert wird zu beginn des Rätsel gespeichert. Dazu wird die Temepratur ausgelesen und abgespeichert. Ziel ist es nun herrasuzufinden wie die Temperatur beinflusst werden kann. Über den Code kann dann herrausgefunden werden ob die Temeratur erhöht oder verringert werden muss.

### Gyro

Für das dritte Teilrätsel müssen die Nutzer herrausfinden das sich der Balken durch kippen der Platine manipulieren lässt. Es gilt also herrauszufinden in welche Richtung und wie weit der Sensehat geneigt werden muss.

## Lösung

Wie in den Kapiteln Code und Rätsel zu sehen ist, müssen die 3 Werte in den korrekten Bereich gebracht werden. Dabei sind 2 Zielwerte fest definiert: Der Joystick Wert ist fest auf 5 eingestellt und der Zielwert für den Gyrosensor ist als 6 definiert. Wobei der Wert 6 einer Neigung von 320-240° entspricht. Der Zielwert für den Temperatur ist hingegen abhängig vom Startwert. Dieser muss um 2° Celsius verringert werden.

### Joystick

Der dargestellte Wert kann durch den eingebauten Joystick verändert werden. Der Stick muss dementsprechend um einige Stufen hoch oder runter gedrückt werden. Sobald der korrekte Wert (5) erreicht ist wird der Balken Grün.

### Temperatur

Die Temperatur muss um 1 Grad Celsius erhöht werden. Dazu reicht im normalfall das auflegen des Fingers auf den entsprechenden Sensor. Da die Tempertur über den Feutigkeitssensor bestimmt wird muss der Finger, oder ein anderes warmes Objekt, auf den mit `Humiditiy` beschriftiten Sensor gelegt werden.

### Gyro

Die Neigung von 320 bis 340 ° zu erreichen muss die obere Kante des Sensehat von einem weg, nach unten, geneigt werden. Darauhin wird der entsprechende Wert an die Funktion weitergegeben und das Teilrästel gelöst.