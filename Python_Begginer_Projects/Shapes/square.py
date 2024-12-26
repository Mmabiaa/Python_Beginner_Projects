# simple square
def accept_square_size(): # A function to accept square size
    size = input('Enter the size of the square: ')
    return size


def validate_square_size(): # A function to validate square size
    size = accept_square_size()

    if size.isdigit():
        size = int(size)
        if size > 1:
            draw_square(size)
        else:
            print('Size must be greater than one!')
    else:
        print('Size must be a digit!')

def draw_square(size): # A function to draw a square

    for i in range(size):
        if i == size-1 or i == 0:
            print('* '*size)
        else:
            print('* '+ '  '*(size-2)+ '*')

def display_square(): # A function that displays the square
    validate_square_size()


if __name__ == '__main__': # main function
  display_square()

    # Author - Mmabiaa
