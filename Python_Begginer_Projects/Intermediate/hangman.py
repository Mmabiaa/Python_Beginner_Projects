import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "challenge"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           
        """,
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    
    while not guessed and tries > 0:
        print(display_hangman(tries))
        print(word_completion)
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print("Sorry, that letter is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job! That letter is in the word.")
                guessed_letters.append(guess)
                word_completion = "".join([guess if letter == guess else word_completion[i] for i, letter in enumerate(word)])
                
            if "_" not in word_completion:
                guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print("Sorry, that's not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        
        else:
            print("Invalid input. Please try again.")

    if guessed:
        print(f"Congratulations! You've guessed the word '{word}' correctly!")
    else:
        print(display_hangman(tries))
        print(f"Sorry, you've run out of tries. The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()