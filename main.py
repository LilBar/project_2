import random
import sys
win_numbers = [7, 11]
lose_numbers = [2, 3, 12]
a = input("If you want to start the game type 'yes', otherwise type 'no'\n")
if a.lower() == "no":
    sys.exit()
else:
    print("Welcome to the craps game!")


def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2


def print_dices(dices):
    die1 = dices[0]
    die2 = dices[1]
    dice_sum = die1 + die2
    print("The sum of dice is {} + {} = {}".format(die1, die2, dice_sum))


value = roll_dice()
print_dices(value)
sum_dices = sum(value)

if sum_dices in win_numbers:
    print("Congratulations! You Won")
    sys.exit()

elif sum_dices in lose_numbers:
    print("You Lost, Try again!")
    sys.exit()
else:
    result = "Continue rolling the dice"
    goal_number = sum_dices
    print("Your goal number is", goal_number)
    print()

while result == "Continue rolling the dice":

    value = roll_dice()
    print_dices(value)
    sum_dices = sum(value)
    if sum_dices == goal_number:
        result = "Congratulations! You Won"
        print("Congratulations!,You Won")
    elif sum_dices == 7:
        result = "You Lost"
        print("You Lost!, \nTry again next time")
