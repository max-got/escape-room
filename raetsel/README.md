# Einleitung

Die `ìnit.py` startet das Spiel. In dieser Datei werden alle Spiele initialisiert und gestartet.

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
