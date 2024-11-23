def calculate():
    n = range(1, 13)
    for i in n:
        print(i, "Times Table")
        print('-----------------------------------')
        for j in n:
            print(i, 'x', j,"=", i*j)
        print()
       
        print('-----------------------------------')

def main():

    calculate()

main()
