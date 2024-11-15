# Simple quiz program
# ----------------------------------------------------------------
def create_quiz():
    
    correct_answer = 0
    guesses = []
    question_number = 1
    for key in Questions:
        print('----------------------------------------------------------------')
        print(key)
        for i in Options[question_number-1]:
            print(i)
        guess = input('Enter a correct answer (A, B, C, or D): ').upper()

        guesses.append(guess)

        correct_answer += check_answer(Questions.get(key), guess)
        question_number += 1
    
    display_scores(correct_answer, guesses)

# ----------------------------------------------------------------
def display_scores(correct_answers, guesses):
    print('-------------------------------------------------------')
    print("RESULTS:")
    print('-------------------------------------------------------')

    print('Answers:', end=' ')
    for i in Questions:
        print(Questions.get(i), end=' ')
    print()

    print('Guesses:', end=' ')
    for i in guesses:
        print(i, end=' ')
    print()

    scores = int((correct_answers / len(Questions)) * 100)
    print("Scores: "+ str(scores) + '%')

# ----------------------------------------------------------------
def check_answer(answer, guess):
    print('----------------------------------------------------------------')
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
# ----------------------------------------------------------------
def play_again():
    print('----------------------------------------------------------------')
    again = input("Do you want to play again (yes or no)?: ").upper()
    if again == 'YES':
        create_quiz()
        return True
    else:
        print("Byeeeeeeeeeee....")
        return False
# ----------------------------------------------------------------
Questions = {
    '1. What is the largest living bird?': 'B',
    '2. What is the largest part of the body?': 'B',
    "3. Which part of thr body don't sleep?": 'A',
    "4. What makes plant food?": 'C',
    "5. Which planet is known as the red plant?": 'D',
    "6. How many legs does a spider has?": 'D',
}
Options = [
    ["A. Eagle", "B. Ostrich", "C. Falcon", "D. Pelican"],
    ["A. Heart", "B. Skin", "C. Spine", "D. Head"],
    ["A. Heart", "B. Kidney", "C. Brain", "D. Liver"],
    ["A. Root", "B. Stem", "C. Leaf", "D. Branches"],
    ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
    ["A. six", "B. nine", "C. seven", "D. eight"]
]

create_quiz()

while play_again():
    create_quiz()