# Palindrome checker  Program

def Start(): # A function to start the program
    print('----Heyyy, Welcome to the Palindrome Checker----')
    print('----------------------------------------------------------------')

    while True: # Loop the program until a says no.
        choice = input('Do you want to start? (Yes or No): ').lower()

        if choice == 'yes':
            main()

        elif choice == 'no':
            print('--------------------------------')
            print('Thanks for time...')
            break

        else:
            print('Please enter yes or no')
    print()
    

def accept_word(): # A function to accept user word.
    word = input('Enter the word or a number: ')

    print('----------------------------------------------------------------')
    return word

def Check_Palindrome(word): # A function to check whether a word is a palindrome or not.

    if word == word[::-1]: # A condition if the reserved word is same as the actual word.

        if word.isdigit():# A condition if the word is a digit for numbers.
            print(f'The number "{word}" is a palindrome.')
        else:
            print(f'The word "{word}" is a palindrome.')

    else: # An otherwise condition for word that are not a palindrome.
        if word.isdigit():# A condition if the word is a digit for numbers.
            print(f'The number "{word}" is not a palindrome.')
        else:
            print(f'The word "{word}" is not a palindrome.')

    print('----------------------------------------------------------------')

def main(): # Main function to take words and check if they are a palindrome or not.

    word = accept_word()
    print('----------------------------------------------------------------')
    Check_Palindrome(word)


if __name__ == '__main__':
    Start()
