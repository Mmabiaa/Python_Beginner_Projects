def accept_country():
    country = input("Enter your country: ")

    if not country.isalpha():  # Check if the input contains only letters
        print('Country must be a string')
        accept_country()
    else:
        validate_country(country)  # Pass the actual country name to validation


def validate_country(country):
    if country.lower() == 'ghana':  # Compare lowercase strings directly
        accept_age()
    else:
        print('You are not a citizen of Ghana')


def accept_age():
    try:
        age = int(input("Enter age: "))  # Attempt to convert input to an integer
        validate_age(age)
    except ValueError:
        print('Age must be a positive number')
        accept_age()  # Call accept_age again instead of accept_country


def validate_age(age):
    if age < 0:  # Check for negative age
        print('Age must be a positive number')
        accept_age()
    elif age >= 18 and age <= 69:  # Eligible range for voting
        print('Eligible to vote')
    elif age > 69:
        print('Too old to vote')
    else:
        print('Too young to vote')


def vote():
    accept_country()


# Start the voting process
vote()
