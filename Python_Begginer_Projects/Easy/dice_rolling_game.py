# Simple Dice Rolling game
import random # random library for generating random numbers

def roll_dice(): # A function to roll the dice
    while True: # while playing the game

            user_input = input("Roll the dice? (y/n): ").lower() # Accepting user inputs in lower case

            if user_input == "y": # Continue if user_input is y

                die1 = random.randint(1,6) # variables for dice
                die2 = random.randint(1,6)

                print(f"You rolled a {die1} and a {die2}")

            elif user_input == "n": # Break from the loop if user input is n
                print("Thanks for playing...")
                break

            else: # Check if user input is invalid
                print("Invalid input")

roll_dice()
