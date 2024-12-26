# Simple quiz that asks questions,  and display results


quiz = {
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


score = 0

def display_Quiz(quiz, score):
    for key, value in quiz.items():
        print(value['question'])
        user_answer = None
        
        user_answer = input('Your answer: ').lower()

        if user_answer ==  value['answer'].lower():
                print('Correct!😁')
                score += 1
                print(f'Your Score = {score}👌')
            
        else:
                print('Wrong!😢')
                print(f'Correct Answer = {value['answer']}')
                print(f'Your Score = {score}👌')

    print(f'Total = {score} / 10')
    percentage = (score / 10) * 100
    print(f'Percentage = {percentage}%')
    print(f'\n Thanks for participating...😁❤️')


display_Quiz(quiz, score)





# Author - Mmabiaa

