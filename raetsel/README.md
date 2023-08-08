# Einleitung

Die `init.py` startet das Spiel. In dieser Datei werden alle Spiele initialisiert und gestartet.

Das Spiel kann mit folgendem Befehl gestartet werden:

```bash
python3 init.py
```

## Aufbau

Die `init.py` hat lediglich zwei relevante Variablen:

```python
#init.py
#...

#kann auch event0, event1, event2, event3 sein
infrarot_sensor = InputDevice("/dev/input/event3")
#GPIO PIN des Buzzers (PWM Modul)
buzzer_pin = 5
raetsel = 1
#...
```

`infrarot_sensor` ist der Sensor, der die Infrarotstrahlen empfängt. Dieser muss auf den Raspberry Pi aufgesteckt werden. Der Sensor muss an den Raspberry Pi angeschlosse. Dazu mehr in der `README.md` im Ordner `raetsel/infrarot_buzzer`.

`buzzer_pin` ist der Pin, an dem der Buzzer angeschlossen ist. Dieser muss an den Raspberry Pi angeschlossen sein. Dazu mehr in der `README.md` im Ordner `raetsel/infrarot_buzzer`.

`raetsel` ist die Variable, die das Level des Spiels angibt. Diese wird in der `init.py` hochgezählt.

## SD-Karte Klonen

Um den Escape Room auch auf anderer Hardware auszuführen oder auf mehereren Raspberries parallel kann die SD-Karte geklnt werden. Dazu gibt es verschiedenen Wege. Getested wurde der Vorgang mit dem Tool Etcher [(Download)](https://etcher.balena.io/#download-etcher) auf Windows. Folgenden Schritte müssen dann befolgt werden:

1. Etcher starten

2. 'Clone drive' auswäheln

3. Entsprechende SD-Karte als Quelle auswählen

4. 'Select 1' klicken

5. In 'select target' eine entsprechende Zielkarte auswählen (wichtig: diese muss mindestens die gleiche größe haben wie die Quellkarte)

6. 'Select 1' klicken

7. 'Flash' zum starten drücken

Danach warten bis der Vorgang abgeschlossen ist und die neue SD-Karte erfüllt alle nötige Softwarevorgaben.