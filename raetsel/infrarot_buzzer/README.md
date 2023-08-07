# Anleitung

Das ist die Anleitung für das Rätsel Infrarot-Buzzer.

## 1. Vorbereitung

Das Rätsel verwendet die Sensoren [KY-006 (Passiver Piezo-Buzzer)](https://sensorkit.joy-it.net/de/sensors/ky-006) und den [KY-022 (Infrarot-Receiver)](https://sensorkit.joy-it.net/de/sensors/ky-022).

Damit die Sensoren verwendet werden können, müssen die folgenden Schritte durchgeführt werden:

1. Die Sensoren müssen an den Raspberry Pi angeschlossen werden. Dazu müssen die Sensoren an die GPIO-Pins angeschlossen werden. Die genaue Pin-Belegung ist in der [Pin-Belegung](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html) zu finden. Das Schema für die Sensoren ist in der folgenden Tabelle zu finden:

**_KY-006_Passiver_Piezo-Buzzer_**

| Raspberry Pi     | Sensor |
| ---------------- | ------ |
| GPIO 24 [Pin 18] | Signal |
| 3,3V [Pin 1]     | +V     |
| GND [Pin 6]      | GND    |

siehe: https://sensorkit.joy-it.net/de/sensors/ky-006

**_KY-022_Infrarot-Receiver_**
|Raspberry Pi | Sensor|
|---|---|
|GPIO15 [Pin 10]|Signal|
|3,3V [Pin 17]|+V|
|GND [Pin 6]|GND|

siehe: https://sensorkit.joy-it.net/de/sensors/ky-022

Die Sensoren können auch an andere Pins angeschlossen werden. In diesem Fall müssen die Pins in der Konfiguration angepasst werden.

2. Die Konfiguration des Raspberry Pi muss angepasst werden. Dazu muss die Datei `/boot/config.txt` mit einem Texteditor geöffnet werden. Am Ende der Datei müssen die folgenden Zeilen hinzugefügt werden:

   ```bash
   dtoverlay=gpio-ir,gpio_pin=17
   ```

   Die Zeile `dtoverlay=gpio-ir` aktiviert den Infrarot-Empfänger. Achtung, gpio_pin muss auf den Pin angepasst werden, an dem der Infrarot-Empfänger angeschlossen ist. In diesem Fall ist der Infrarot-Empfänger an Pin 17 angeschlossen.

   ```bash
   sudo reboot
   ```

   Nach dem Neustart des Raspberry Pi sollte der Infrarot-Empfänger aktiviert sein.

   ```bash
   sudo apt-get install ir-keytable -y
   ```

   Mit dem Befehl `sudo ir-keytable` kann der Infrarot-Empfänger getestet werden. Wenn der Infrarot-Empfänger korrekt angeschlossen ist, sollte der Befehl `sudo ir-keytable` die folgende Ausgabe liefern:

   ```bash
   Found /sys/class/rc/rc0/ (/dev/input/event0) with:
   ```

   Wenn der Infrarot-Empfänger nicht korrekt angeschlossen ist, sollte der Befehl `sudo ir-keytable` die folgende Ausgabe liefern:

   ```bash
   No devices found
   ```

   Wenn der Infrarot-Empfänger korrekt angeschlossen ist, kann der Infrarot-Empfänger mit dem Befehl `sudo ir-keytable -t -s rc0` getestet werden. Wichtig hierbei ist, dass das `rc0` auch `rc1` oder `rc2` sein kann. Die Ausgabe sollte wie folgt aussehen:

   ```bash
   Ereignisse werden getestet. Bitte drücken Sie STRG-C, um abzubrechen.

   20495.413718: Lirc Protokoll(other): scancode = 0x25 umschalten=1
   20495.413750: Ereignistyp EV_MSC(0x04): Scancode = 0x25
   20495.413750: Ereignistyp EV_SYN(0x00).
   20496.141707: Lirc Protokoll(other): scancode = 0x24 umschalten=1
   20496.141736: Ereignistyp EV_MSC(0x04): Scancode = 0x24
   20496.141736: Ereignistyp EV_SYN(0x00).
   20496.877700: Lirc Protokoll(other): scancode = 0x26 umschalten=1
   20496.877725: Ereignistyp EV_MSC(0x04): Scancode = 0x26
   20496.877725: Ereignistyp EV_SYN(0x00).
   20503.989638: Lirc Protokoll(other): scancode = 0xf umschalten=1
   20503.989675: Ereignistyp EV_MSC(0x04): Scancode = 0x0f
   20503.989675: Ereignistyp EV_SYN(0x00).
   ```

   Wenn das nicht der Fall sein sollte, ist es möglich zu verwendeten Protokolle mit dem Befehl `sudo ir-keytable -c -p all -t -s rc0` zu auf "alle Protokolle" zu setzen.

   **_Jetzt kommt der schwierige Part._**

   Wichtig ist, dass ein Protokoll genutzt wird, welches zu dem Sender passt. Es ist unwahrscheinlich, dass ein Protokoll vorinstalliert ist, welches zu dem Sender passt. Aus diesem Grund ist es empfehlenswert eine eigenes Protokoll zu basteln. Wie solch ein Protokoll aussieht ist in der `samsung.toml` zu finden.

   Nun muss das erstellte Protokoll genutzt werden, um die Tasten des Senders zu erkennen. Dazu muss der Befehl `sudo ir-keytable -c -p <Protokoll> -t -s rc0` ausgeführt werden. Wichtig hierbei ist, dass das `rc0` auch `rc1` oder `rc2` sein kann.

   Beispiel:

   ```bash
   sudo ir-keytable -c -p nec -w ./Desktop/sensor/samsung.toml -p imon -w  ./Desktop/sensor/secret.toml -v -s rc1
   ```

   **_ACHTUNG: HIER WERDEN 2 PROTKOLLE VERWENDET!_**
   Warum das so ist, wird im Lösungs-Teil erklärt.

   Wenn nun eine Taste auf der Fernbedienung gedrückt wird, und das Protokoll richtig ist, sollte alles funktionieren.

   Wichtig ist, dass die `MY_KEYMAP.toml` Datei bereit liegt, da sie für weitere Schritte benötigt wird.

   Weitere Informationen sind unter folgenden Links zu finden:

   - https://wiki.ubuntuusers.de/ir-keytable/#Keymap
   - https://manpages.debian.org/testing/ir-keytable/rc_keymap.5.en.html

## Code

### Dateien

Das Rätsel teilt sich in 5 Dateien auf: `escape.py`, `events.py`, `music.py`, `sequence.py` und `utils.py`.

#### escape.py

Die `escape.py` Datei ist die Hauptdatei. In dieser Datei wird das Spiel gestartet und die anderen Dateien importiert.

#### events.py

Die `events.py` Datei enthält die Reihenfolge des Inputs auslesen, Musik abspielen usw.

Beispiel:

```python
def toLongEvent(pwm) -> None:
    play_tooLong_music(pwm)
    console.clear()
    console.print(
        "Die Eingabe war zu lang. Versuche es erneut."
        + "\n"
        + ":bomb: Deine bisherige Eingabe wird gelöscht. :bomb:"
    )
```

In diesem Beispiel wird die Funktion `toLongEvent` definiert. Diese Funktion wird aufgerufen, wenn die Eingabe zu lang ist. In dieser Funktion wird die Musik abgespielt und eine Nachricht ausgegeben.

#### music.py

Die `music.py` Datei enthält die Funktionen, welche die Musik abspielen und die enstprechenden Melodien (dict) enthalten.

Beispiel:

```python
tooLong_music = {
    'melody': [262, 294, 262, 294, 262],
    'duration': 0.2,
    'pause': 0.1,
}
#...
def play_tooLong_music(pwm) -> None:
    """Spielt die Melodie für zu lange Eingaben ab."""
    play_music(melody =tooLong_music['melody'], duration=tooLong_music['duration'], pause=tooLong_music['pause'], pwm = pwm)
```

In diesem Beispiel wird die Melodie für zu lange Eingaben definiert. Diese Melodie wird in der Funktion `play_tooLong_music` abgespielt.

#### sequence.py

Die `sequence.py` Datei enthält die Funktionen, welche die Sequenz erstellt und ausließt.

**_ACHTUNG_**
Lass dich nicht von der `seqGen()` Funktion verwirren. Diese ist absichtlich so geschrieben, dass sie nicht verständlich ist. Sie ist nur dafür da, dass die Sequenz nicht erraten werden kann.

Die "originale" `seqGen()` Funktion ist als Kommentar in der Datei zu finden.

#### utils.py

Die `utils.py` Datei enthält die Funktionen, welche ab und zu benötigt werden.

Beispiel:

```python
def int_check(s : str) -> bool:
    """Checks if the string s is an integer"""
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True
```

In diesem Beispiel wird die Funktion `int_check` definiert. Diese Funktion prüft, ob der String `s` eine Zahl ist. Wenn ja, wird `True` zurückgegeben, wenn nicht, wird `False` zurückgegeben.

### Ablauf

Der Ablauf des Programms ist in der `escape.py` Datei zu finden.

```python
def readInputEvent(device: InputDevice):
    sequence = []
    # Schleife, die auf Tastendruck wartet
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == 1:
                data = categorize(event)
                makeSignal(k2n(data.keycode), pwm)

                # Ärgerlich, dass man pressed_key nicht lesen kann. Was können wir denn da machen?
                pressed_key = obfuscated_func(data.keycode)

                print("Du hast die Taste: '", pressed_key, "' gedrueckt")

                sequence.append(data.keycode)

                if len(sequence) > 10:
                    exc_event(pwm, 2)
                    sequence = []

                # Was heißt denn [-1]?
                if len(sequence) == 10 and sequence[-1] == "KEY_OK":
                    if is_correct_sequence(sequence, GPIO_P1N):
                        exc_event(pwm, 1)
                    else:
                        exc_event(pwm, 0)
                    sequence = []
```

In diesem Beispiel ist die Funktion `readInputEvent` zu sehen. Diese Funktion liest die Eingabe des Spielers ein und speichert diese in der `sequence` Variable. Wenn die Eingabe zu lang ist, wird die `exc_event` Funktion mit dem Parameter `2` aufgerufen. Wenn die Eingabe richtig ist, wird die `exc_event` Funktion mit dem Parameter `1` aufgerufen. Wenn die Eingabe falsch ist, wird die `exc_event` Funktion mit dem Parameter `0` aufgerufen.

Wobei `0` für eine falsche Eingabe steht, `1` für eine richtige Eingabe und `2` für eine zu lange Eingabe.
Das wurde einfach nur so gemacht, dass bei einfachen lesen des Codes nicht direkt klar ist, was die Funktion macht.

## Rätsel

Das eigentliche Rätsel besteht daraus, dass der Spieler die richtige Sequenz herausfinden muss. Dazu muss er die Tasten auf der Fernbedienung drücken. Wenn er die richtige Sequenz herausgefunden hat, muss er die OK Taste drücken. Wenn die Sequenz richtig ist, wird die `exc_event` Funktion mit dem Parameter `1` aufgerufen. Wenn die Sequenz falsch ist, wird die `exc_event` Funktion mit dem Parameter `0` aufgerufen.

Das Problem ist jedoch, dass die Sequenz nicht einfach so herausgefunden werden kann. Dazu muss der Spieler die `seqGen` Funktion in der `sequence.py` Datei verstehen. Diese Funktion ist jedoch absichtlich so geschrieben, dass sie nicht verständlich ist. Sie ist nur dafür da, dass die Sequenz nicht erraten werden kann.

**_Aber wir lösen wir nun das Rätsel?_**

## Lösung

Um die Lösung des Rätsels zu verstehen, müssen wir uns die Funktion `is_correct_sequence` in der `sequence.py` Datei anschauen.

```python
def is_correct_sequence(sequence: list[str], expected_sequence: list[str]) -> bool:
    """Überprüft, ob die Sequenz korrekt ist
    sequence: Die Sequenz, die überprüft werden soll
    expected_sequence: Die erwartete Sequenz
    Wenn die Sequenz korrekt ist, wird True zurückgegeben, ansonsten False
    """
    x = ["S0VZX0E=", "S0VZX0I=", "S0VZX0M="]

    if sequence == expected_sequence or any(
        [u.b64decode(key).decode() in sequence for key in x]
    ):
        return True
    else:
        return False
```

Dabei soll besonderes Augenmerk auf die Variable `x` gelegt werden. Diese Variable enthält 3 Base64 Strings. Diese Strings sind die Lösung des Rätsels. Wenn der Spieler diese Strings in die Sequenz eingibt, wird die Sequenz als richtig erkannt.

Diese Strings sind die gemappten Daten aus der `secret.toml` Datei, welche die Daten der Face ID enthält.

```toml
[[protocols]]
name = "secret"
protocol = "imon"
variant = "imon-pad"
[protocols.scancodes]
0x1fffffff = "KEY_A"
0x3fffffff = "KEY_B"
0x7fffffff = "KEY_C"
```

Wenn die Face ID Entsperrung an den Sensor gehalten wird, erhält der Sensor die Daten `0x1fffffff`, `0x3fffffff` und `0x7fffffff`. Diese Daten werden dann als `KEY_A`, `KEY_B` und `KEY_C` gemappt. Dann Base64 encoded und in der `x` Variable gespeichert. Das ist der Grund, warum die Face ID Entsperrung funktioniert.

Das Base64 Encoding muss manuell gemacht werden. Das könnte man noch automatisieren, aber du brauchst ja auch noch was zu tun. ;)
