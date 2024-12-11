import random

responses = [
    "Yes, definitely.",
    "As I see it, yes.",
    "Reply hazy, try again.",
    "Cannot predict now.",
    "Do not count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

def magic_8_ball():
    print("Welcome to the Magic 8 Ball! Ask a yes/no question.")
    
    while True:
        question = input("Ask your question (or type 'quit' to exit): ")
        
        if question.lower() == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        
        if question.strip() == "":
            print("Please ask a valid question.")
            continue
            
        # Get a random response
        answer = random.choice(responses)
        print("Magic 8 Ball says:", answer)

# Run the program
magic_8_ball()
