
from functools import reduce as _reduce
from random import randint as _randint, seed as _seed

def int_check(s : str) -> bool:
    """Checks if the string s is an integer"""
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

def obfuscated_func(p : str) -> str:
    """Randomizes the string p"""
    _seed(p)
    g = _reduce(lambda g, c: g + chr(ord(c) + _randint(0, 25)), p, "")
    return g


