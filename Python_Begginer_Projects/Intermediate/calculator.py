# A simple calculator program
def Menu(): # Menu to hold menu options and user choices
    menu_options = (1,2,3,4,5)

    user_choice = None

    print("\n Menu \n 1. Addition 2. Subtraction 3. Multiplication 4. Division 5 Exit.")

    while True:
        # Repeat the loop till user option is true.
        try:
            user_choice = int(input('Enter a choice from the menu (1-5): '))
            if user_choice not in menu_options:
                print("Invalid input")
                continue

        except ValueError:
            print("Please enter a valid choice")
            continue

        return user_choice


def get_user_values(): # A function to store user values for calculators
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    return num1, num2

def Calculate(user_choice, num1, num2): # A function that calculates base on user values and menu choices

    if user_choice == 1:
        return f'{num1} + {num2} = {num1 + num2}'

    elif user_choice == 2:
        return f'{num1} - {num2} = {num1-num2}'

    elif user_choice == 3:
        return f'{num1} x {num2} = {num1*num2}'

    elif user_choice == 4:
        if num2 == 0:
            print("Division by zero is invalid")
        else:
            return f'{num1} ÷ {num2} = {num1/num2}'

def Main(): # A main function to run and test the program
    while True:
        user_choice = Menu()

        if user_choice == 5:
            print('Thanks for using this program...😁')
            break

        num1, num2 = get_user_values()

        result = Calculate(user_choice, num1, num2)

        print(result)

Main() # CAll the Main function to run the program
# Author - Mmabiaa
