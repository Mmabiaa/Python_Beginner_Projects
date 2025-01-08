
import random # A library to generate random choices

# variables to store options
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {ROCK:'🪨', PAPER:'📃', SCISSORS:'✂️'} # A dictionary to store option keys with emoji values
options = tuple(emojis.keys()) # A tuple to store option values



def get_user_choice():# A function to return a user choice

        user_input = input("Rock, paper, or scissors? (r/p/s): ")

        if user_input in options:
            return user_input
        else:
            print("Invalid input")



def display_choices(cpu, user_input): # A function that displays the choices (cpu, user_input)

    print(f"You chose {emojis[user_input]}")
    print(f"Computer chose {emojis[cpu]}")


def determine_winner(cpu, user_input): # A function that determines the winner

    if ((user_input == ROCK and cpu == SCISSORS) or
        (user_input == SCISSORS and cpu == PAPER) or
        (user_input == PAPER and cpu == ROCK)):
            print("You won!🥳")
    elif(user_input == cpu):
                print("You tie!😎")
    else:
                print("You lose!😢")


def Game():# A function to return various functions to start the game.
    while True:
        user_input = get_user_choice()

        cpu = random.choice(options)

        display_choices(cpu, user_input)

        determine_winner(cpu, user_input)

        Continue = input("Do you want to continue (y/n)😊: ").lower()

        if Continue == 'n':
            print("Thanks for playing!😁")
            break

# Calling the Game function to initialize the program.
Game()
