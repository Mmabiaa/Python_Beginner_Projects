# A simple program that helps users to get a password idea.
import random
import string

def Storage():
    characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

    options = ['y', 'n']

    return characters, options

def get_password(characters, options):

    while True:
        user_choice = input('Do you want to generate a new password (y/n): ').lower()

        if user_choice not in options:
            print('Enter a valid choice (y/n)')


        else:
            if user_choice == 'y':
                password_length = int(input('Enter password length: '))
                random.shuffle(characters)

                password = []

                for x in range(password_length):
                    password.append(random.choice(characters))

                random.shuffle(password)

                password = ''.join(password)

                print(password)

            else:
                print('Thanks for using this program...😁')
                break

def Main():
    characters, options = Storage()

    get_password(characters, options)

Main()


