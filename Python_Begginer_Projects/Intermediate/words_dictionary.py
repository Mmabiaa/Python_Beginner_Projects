from PyDictionary import PyDictionary

# A simple word dictionary program

dictionary = PyDictionary()



def Synonym(word):
    print(dictionary.synonym(word))

def Antonym(word):
    print(dictionary.antonym(word))

def Quit():
    print('Thanks for using this software...😁👌')

def Meaning(word):
    print(dictionary.meaning(word))


def Main():

    options = (1, 2, 3)

    print('A Simple Word Dictionary Program')

    while True:

        print('Menu \n 1. Get Meanings 2. Get Synonyms 3. Get Antonyms 4. Quit')


        user_choice = None
        try:
            user_choice = int(input('Enter a choice: '))


            if user_choice in options:
                word = input('Enter a word: ')
                
                if user_choice == 1:
                    Meaning(word)
                elif user_choice == 2:
                    Synonym(word)
                else:
                    Antonym(word)
                    
            elif user_choice == 4:
                Quit()
                break
                
            else:
                print('Enter a choice(1-4)')

        except ValueError:
            print('Invalid Option!')
        
        print('')

# Calling the main function
Main()
# Author - Mmabiaa
