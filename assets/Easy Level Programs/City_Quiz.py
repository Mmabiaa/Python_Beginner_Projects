# Simple quiz that asks questions,  and display results


def Quiz_Question(): # A function that stores quiz questions and answers and return quiz and score

        score = 0

        quiz = {# A dictionary containing quiz questions and answers
    'questions 1':{
        'question': 'What is the capital of France?:  ',
        'answer': 'Paris'
    },
    'questions 2':{
        'question': 'What is the capital of Germany?:  ',
        'answer': 'Berlin'
    },
    'questions 3':{
        'question': 'What is the capital of Canada?:  ',
        'answer': 'Toronto'
    },
    'questions 4':{
        'question': 'What is the capital of Italy?:  ',
        'answer': 'Rome'
    },
    'questions 5':{
        'question': 'What is the capital of Spain?:  ',
        'answer': 'Madrid'
    },
    'questions 6':{
        'question': 'What is the capital of Portugal?:  ',
        'answer': 'Lisbon'
    },
    'questions 7':{
        'question': 'What is the capital of Switzerland?:  ',
        'answer': 'Bern'
    },
    'questions 8':{
        'question': 'What is the capital of Netherland?:  ',
        'answer': 'Amsterdam'
    },'questions 9':{
        'question': 'What is the capital of Austra?:  ',
        'answer': 'Vienna'
    },'questions 10':{
        'question': 'What is the capital of Russia?:  ',
        'answer': 'Moscow'
    }
    }
        return score, quiz




def display_Quiz(quiz, score): # A function that displays quiz and results

    for key, value in quiz.items(): # A loop to iterate through the quiz items and display (questions and answers)
        print(value['question']) # Printing each question in the quiz
        user_answer = None

        user_answer = input('Your answer: ').lower()

        # conditions to validate results
        if user_answer ==  value['answer'].lower():
                print('Correct!😁')
                score += 1
                print(f'Your Score = {score}👌')
                print(' ')

        else:
                print('Wrong!😢')
                print(f'Correct Answer = {value['answer']}')
                print(f'Your Score = {score}👌')
                print(' ')

    print(f'\n Total = {score} / 10')
    percentage = (score / 10) * 100
    print(f'Percentage = {percentage}%')
    print(f'\n Thanks for participating...😁❤️')


def main(): # main function to run the program.
      score, quiz = Quiz_Question()

      display_Quiz(quiz, score)

main() # calling the main function to run the program.







