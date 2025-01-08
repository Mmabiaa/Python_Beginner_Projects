def binary_search(list, element):
    midpoint = 0
    start = 0
    end = len(list)
    steps = 0

    while start <= end:
        print(f'Steps {steps}: {list[start:end+1]}')

        steps +=1

        midpoint = (start + end) // 2

        if element == list[midpoint]:
            return midpoint
        elif element < list[midpoint]:
            end = midpoint - 1
        else:
            start = midpoint +1

        if element in list:
            print("Target found: ",True)
        else:
            print("Target not found: ",False)

    return -1

def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,]
    target = int(input('Enter a target: '))

    binary_search(my_list, target)

main()





