from random import choice as _choice
import base64 as u


def is_correct_sequence(sequence, expected_sequence): #list[str]) -> bool:
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


def seqGen():
    w = [
        "S0VZX09L",
        "S0VZX05VTUJSSUNfMA==",
        "S0VZX1VQ",
        "S0VZX1VQ",
        "S0VZX05VTUJSSUNf",
        "S0VZX1VQ",
        "S0VZX1VQ",
        "S0VZX0JP",
    ]
    h = [
        _choice(
            [
                u.b64decode("S0VZX05VTUVSSUM=").decode() + "_" + str(x)
                for x in range(1, 10)
            ]
        )
        for _ in range(9)
    ]
    x = int(
        (((((((((1 + 1) - 1) + 1) - 1) + 1) - 1) + 1) - 1) + 1)
        / (((((((((1 + 1) - 1) + 1) - 1) + 1) - 1) + 1) - 1) + 1)
        - 1
    )
    f = [_choice([key]) for key in h]
    l = w[x]
    z = f + ["KEY_OK"]
    return [u.b64decode(key).decode() if key in w else key for key in z]


"""
first_9_keys = [_choice(["KEY_NUMERIC_{}".format(i) for i in range(9)] + ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]) for i in range(9)]
last_key = "KEY_OK"

expected_sequence = first_9_keys + [last_key]
"""
