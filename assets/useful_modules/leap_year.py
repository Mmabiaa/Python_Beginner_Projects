def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap year 😁🥳')
            else:
                print('Not leap year 😢')
        else:
            print('Leap year 😁🥳')
    else:
        print('Not leap year 😢')

def main():
    while True:
        year = int(input('Enter a year: '))
        is_leap_year(year)

        options = ('y', 'n')
        Continue = input('Continue (y/n): ').lower()
        if Continue not in options:
            print('Invalid option')

        else:
            if Continue == 'y':
                print('')
            else:
                print('Thanks for using the program...😁👌')

main()