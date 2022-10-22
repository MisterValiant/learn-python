# Roll dices randomly
#  Dice method: roll() - rolls a tuple

import random

numbers = (1, 2, 3, 4, 5, 6)


def roll():
    return random.choice(numbers)


dice_number = roll()
print(dice_number)
