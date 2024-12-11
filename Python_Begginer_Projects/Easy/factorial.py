number = int(input('Enter a number: '))

def Cal(number):
    if(number == 1):
        return 1
    else:
        return number * Cal(number - 1)

a = Cal(number)
print(number, '! =', a)
