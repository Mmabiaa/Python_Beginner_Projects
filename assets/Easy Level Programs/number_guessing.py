# A simple number guessing game using python.
import random # For random numbers

def number_guessing():
    number = random.randint(1,100)
    while True:

        try:
            guess = int(input("Guess a number from 1 to 100: "))

            if number == guess:
                print("Congratulations! You guessed the number!")
                break
            elif number > guess:
                print("Too low!")
            else:
                print("Too high!")
            

        except ValueError:
            print("Enter a valid number")

number_guessing()