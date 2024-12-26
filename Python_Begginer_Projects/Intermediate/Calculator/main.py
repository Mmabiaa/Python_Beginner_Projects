from Calculator import calculate # import a class module I wrote in Calculator.py called calculate

signs = { # A dictionary to store signs according to user choices from menu
    1:'+',
    2:'-',
    3:'x',
    4:'/'
}

def display_menu(): # A method to display menu options to users
    print(
        '''---Menu---
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Quit
        
        '''
    )
    accept_user_choice() # Calling a function that accepts user menu choices.

def accept_user_choice(): # A Method to accept user choices

    user_choice = input('Enter a choice from (1 - 5): ') # a prompt variable to accept user choice and store them as string

    if user_choice.isdigit(): # a condition to check if the user choice is a digit or not.
        user_choice = int(user_choice) # converting user choices from str to int after being a digit
        validate_user_choice(user_choice) # calling the validation method to validate if user choice is true.

    else: # An else statement to prompt errors
        print('Invalid user choice...')
        accept_user_choice() # using recursion method to run this method to re-accept the user choice till conditions are met




def validate_user_choice(choice): # a method to validate user choices for the menu options
    if 0 < choice < 5: # choices from users should be from (1 - 5) but 5 is an exception to quit the program
        display_results(choice) # display results after conditions are met


    elif choice == 5: # quit the program if a uer choice is 5
        print('Quiting...')
        quit()

    else: # a prompt condition to alert users to enter a choice from 1-5
        print('Choice must be from 1 - 5')
        accept_user_choice() # calling this method to accept new user choices

def assign_user_choice_to_menu_option(x, y,choice): # a method to assign various choices to appropriate calculations
    
    cal = calculate(x, y) # creating an object for the class calculate to be used in calling various class methods.

    if choice == 1:
        return cal.add()
    elif choice == 2:
        return cal.sub()
    elif choice == 3:
        return cal.mul()
    else:
        return cal.div()


def accept_values(): # A method to accept user values for calculations

        x = input('Enter value 1: ')
        y = input('Enter value 2: ')

        if (x and y).isdigit(): # Checking if valuses are digit then it's converted into float
            x = float(x)
            y = float(y)

        else: # a case where values are not digits
            print('Please enter a digit / a number... ')
            accept_values()
        return x, y

def display_results(choice):# method to display the answer
    x, y = accept_values()

    answer = assign_user_choice_to_menu_option(x, y, choice) # calling this method to assign user choice to right menu option

    for key, pair in signs.items(): # using a for loop to print the answer with the appropriate sign
        if key == choice:
            print(f'{x} {pair} {y} = {answer}')





def main(): # main loop
    print('--Calculator--')
    while True:
        display_menu() # calling this function to start the process

        again = input('Do you want to continue (n / y): ').lower() # a prompt to ask users for continuation
        if again != 'y':
            quit()
            break
        else:
            print(' ')


if __name__ == '__main__': # running from the mainloop...
    main()

#mMabiaa