# Raspberry Escape Room

Dieses Repository enthält die kleinen Programme und die Dokumentation für das Raspberry Escape Room Projekt des Moduls "WPM Industrie 4.0 SoSe 2023" an der TH Brandenburg.

## Inhalt

- [Raspberry Escape Room](#raspberry-escape-room)
  - [Inhalt](#inhalt)
  - [Projektbeschreibung](#projektbeschreibung)
  - [Hardware](#hardware)
  - [Programme](#programme)
  - [Dokumentation](#dokumentation)
  - [Verwendung](#verwendung)
  - [Autoren](#autoren)

## Projektbeschreibung

Das Projekt enstannt aus einem Workshops zum Summer Coding Festival(2023) an der TH Brandenburg. Ziel des Projektes/Workshops war es Schüler für das Thema der Sensorik zu begeistern. Dazu wurde ein "digitaler Escape Room" entwickelt, in welchem die Teilnehmer mehrere Rätsel lösen müssen, um die Möglichkeiten der Sensorik zu verstehen und natürlich um Spaß zu haben. Keiner hat Freude an trockenen Theorievorträgen.

## Hardware

Für dieses Projekt wurden mehrere Raspberry Pi 4 Model B mit 4GB RAM verwendet.
Folgende Sensoren wurden verwendet:

- [SenseHat](https://www.raspberrypi.org/products/sense-hat/)
- [Passive Piezo-Buzzer](https://sensorkit.joy-it.net/en/sensors/ky-006)
- [Infrarot-Abstandssensor](https://sensorkit.joy-it.net/en/sensors/ky-032)
- [Infrared receiver](https://sensorkit.joy-it.net/en/sensors/ky-022)
- [Rotary encoder](https://sensorkit.joy-it.net/en/sensors/ky-040)
- Webcam

## Rätsel

Die Rätsel sind in Python geschrieben und sind im Ordner `raetsel` zu finden. Momentan sind 6 Rätsel implementiert, welche in der Reihenfolge der Nummerierung gelöst werden müssen.

## Dokumentation

1. [Init](/raetsel/README.md)
2. [Drehschalter (Fragen)](/raetsel/drehschalter/README.md)
3. [Infrarot + Abstandssensor](/raetsel/infrarot_abstand/README.md)
4. [SenseHat Simon Says](/raetsel/sensehat_simon/README.md)
5. [SenseHat 3in1](/raetsel/sensehat_3in1/README.md)
6. [Hand Recognition](/raetsel/hand_recognition/README.md)
7. [Infrarot + Buzzer](/raetsel/infrarot_buzzer/README.md)

## Verwendung

Um die Rätsel zu starten, muss das Programm `init.py` ausgeführt werden. Dieses Programm startet die Rätsel in der richtigen Reihenfolge und wechselt bei erfolgreicher Lösung zum nächsten Rätsel. Die Rätsel können auch einzeln gestartet werden, indem die jeweilige `main.py` ausgeführt wird.

## Autoren

- [**Max Gottschalk**](https://github.com/max-got)
- [**Gregor Rose**](https://github.com/Grulk47)
- [**Jonas Bethwell**](#)
- [**Mirko Reefschläger**](#)
