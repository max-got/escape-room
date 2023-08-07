# Einleitung

Für dieses Rätsel wird ein SenseHat benötigt. Dieser wird auf den Raspberry Pi aufgesteckt. Die SenseHat Bibliothek muss installiert sein. Dies kann mit folgendem Befehl getan werden:

```bash
sudo apt-get install sense-hat
```

Das Programm kann nun mit folgendem Befehl gestartet werden:

```bash
python3 escape.py
```

## Aufbau

Steck den SenseHat auf den Raspberry Pi. Fertig ist der Aufbau.

## Programm

Für dieses Rätsel ist im Prinzip nur die `escape.py` wichtig. Diese startet das Spiel und ruft die anderen Funktionen auf. Die anderen Dateien sind nur Hilfsdateien, welche die Funktionen für das Spiel enthalten.

Eine richtige Anleitung wird nicht benötigt, da darauf geachtet wurde, dass in der `escape.py` alles erklärt wird.

Die main Funktion hat folgende Parameter:

`curr_lvl`: Der aktuelle Level des Spiels. Dieser wird in der `escape.py` hochgezählt.

`speed`: Die Zeit, die ein Symbol angezeigt wird. Je niedriger die Zeit, desto schneller das Spiel.

`speed_factor`: Der Faktor, um den die Zeit pro Level verringert wird. Je niedriger der Faktor, desto schneller das Spiel.

`append_factor`: Der Faktor, um den die Länge der Sequenz pro Level erhöht wird. Je höher der Faktor, desto mehr Symbole werden pro Level hinzugefügt.
