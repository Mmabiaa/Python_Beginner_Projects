# Simple Dice Rolling game
import random

def create_dice():
    dice_faces = {
        1:{ """
        +-------+
        |   1   |
        |   ●   |
        |       |
        +-------+
        """},
        2:{ """
        +-------+
        | ●     |
        |   2   |
        |     ● |
        +-------+
        """},
        3:{ """
        +-------+
        | ●  3  |
        |   ●   |
        |     ● |
        +-------+
        """},
        4:{ """
        +-------+
        | ●   ● |
        |   4   |
        | ●   ● |
        +-------+
        """},
        5: {"""
        +-------+
        | ● 5 ● |
        |   ●   |
        | ●   ● |
        +-------+
        """},
        6:{ """
        +-------+
        | ●   ● |
        | ● 6 ● |
        | ●   ● |
        +-------+
        """}
    }
    return dice_faces

def roll_dice(dice_faces):

    options = ['y', 'n']

    while True:
        roll = input('Roll the dice (y/n): ')

        if roll not in options:
            print('Enter a valid input (y/n) \n')
        
        else:

            if roll == 'n':
                   print('Thanks for playing...😁👌')
                   break

            else:

                dice1 = random.randint(1,6)
                dice2 = random.randint(1,6)

                print(f'Dice rolled: {dice1} and {dice2}')
                print('\n'.join(dice_faces[dice1]))
                print('\n'.join(dice_faces[dice2]))





def main():
    dice_faces = create_dice()
    roll_dice(dice_faces)

main()
