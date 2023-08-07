from rich.console import Console as _Console

from time import sleep as _sleep
from tqdm import tqdm as _tqdm
from random import choice as _choice

from .music import play_fail_music, play_success_music, play_tooLong_music


console = _Console()


def checking_sequence() -> None:
    console.clear()
    print("CHECKING SEQUENCE")
    for i in _tqdm(range(15)):
        _sleep(0.5)


# Das sieht aber spanned aus. Was macht das? ;)
def give_hint(string) -> str:
    key = _choice(string)
    index = string.index(key)

    return f"Die {index + 1}. Taste ist {key}"


def exc_event(pwm, event: int) -> None:
    """Logs the event"""
    if event == 2:
        toLongEvent(pwm)
    elif event == 1:
        successEvent(pwm)
    elif event == 0:
        failEvent(pwm)


def toLongEvent(pwm) -> None:
    play_tooLong_music(pwm)
    console.clear()
    console.print(
        "Die Eingabe war zu lang. Versuche es erneut."
        + "\n"
        + ":bomb: Deine bisherige Eingabe wird gelöscht. :bomb:"
    )


def successEvent(pwm) -> None:
    play_success_music(pwm)
    console.print("You have escaped the prison. Congratulations!", style="green")
    console.print("YOU WIN", style="green")


def failEvent(pwm) -> None:
    play_fail_music(pwm)
    console.clear()
    console.print(
        "Du hast es nicht geschafft aus dem Escape Room zu entkommen. Versuche es erneut.",
        style="red on white",
        justify="center",
    )
