import time
from sense_hat import SenseHat
from .sequence import Sequence
from .ledHelper import LEDHelper
from .symbols import symbols

def main(
        curr_lvl:int = 1,
        speed:float = 1,
        speed_factor:float = 0.7,
        append_factor:int = 1,
        lvls_to_win:int = 5
        ) -> None:
    """
    Main function of the game.
    :param curr_lvl: The current level of the game. 
    :param speed: The time to display each symbol. The lower the time, the faster the game.
    :param speed_factor: The factor by which the speed of the game increases. The lover the factor, the faster the game.
    :param append_factor: The factor by which the length of the sequence increases each level. The higher the factor, the more symbols are added to the sequence each level.
    """
    sense = SenseHat()
    sequenceHelper = Sequence(symbols)
    ledHelper = LEDHelper(sense)


    for i in range(3, 0, -1):
        ledHelper.show_letter(str(i))
        time.sleep(1)

    # Display the level on the LED matrix.
    ledHelper.show_lvl(curr_lvl)

    # Display the sequence on the LED matrix.
    pressed_sequence = []

    # The time to display each symbol but must be atleast 0.1
    sec = max(0.1, speed)

    #seq_length == curr_lvl but must be at least 3
    seq_length = max(3, curr_lvl)

    # Generate a sequence of symbols.
    sequenceHelper.generate(seq_length)

    # Display the sequence on the LED matrix.
    ledHelper.show_sequence(sec, sequenceHelper.valuesAsArray())

    # Track the lvls won
    lvls_won = 0

    print(sequenceHelper.getSequence())	
    while lvls_won != lvls_to_win: #True:
        # Check if the player has won
        if lvls_won == lvls_to_win:
            # Show won instance
            ledHelper.won(curr_lvl)
            # Return True to indicate that the player has won
            return True
        for event in sense.stick.get_events():
            if event.action == "pressed":
                pressed_sequence.append(event.direction)
                if pressed_sequence == sequenceHelper.getSequence()[:len(pressed_sequence)]:
                    ledHelper.success()
                    if len(pressed_sequence) == sequenceHelper.getLength():
                        # Increase the level
                        curr_lvl += 1

                        # Increase the speed
                        sec = sec * speed_factor

                        # Increase the lvls won
                        lvls_won += 1

                        # Show won instance
                        ledHelper.won(curr_lvl)

                        # Add as many symbols to the sequence as the append_factor
                        for i in range(0, append_factor):
                            sequenceHelper.addSymbol()

                        
                        print(sequenceHelper.getSequence())
                        # Display the sequence on the LED matrix.
                        ledHelper.show_sequence(sec, sequenceHelper.valuesAsArray())

                        # Reset pressed_sequence
                        pressed_sequence = []
                else:
                    # Show loose instance
                    ledHelper.loose()

                    # Start over from level 1 and keep the speed
                    main(1, 1, speed_factor, append_factor, lvls_to_win)
                    return False
        time.sleep(0.1)
    return True