def Square(s):
    for i in range(s):
        if i == 0:  # First row
            print('*')
        elif i == s - 1:  # Last row
            print('* ' * s)
        else:  # Middle rows
            print('*' + ' ' * (2 * i - 1) + '*')
def check_length():
    while True:
        length = input('Enter the length of the triangle: ')
        if length.isdigit():
            length = int(length)
            if length > 1:
                Square(length)
            else:
                print('Length must be greater than one.')
        else:
            print('Please enter a digit.')


check_length()

if __name__ == '__main__':
    check_length()


