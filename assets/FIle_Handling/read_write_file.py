
 # r ----> read
  # w ----> write
   # a ----> append
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(content)  # Print content to the console
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_file(filename):
    try:
        text = input("Enter a text to be written to the file: ")
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Text successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_file(filename):
    try:
        text = input("Enter a text to be appended to the file: ")
        with open(filename, 'a') as file:
            file.write(text)
        print(f"Text successfully appended to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        while True:
            user_choice = int(input('Menu\n 1. Write File \n 2. Read File \n 3. Append File \n 4. Exit\nEnter your choice (1-4): '))

            filename = 'C:\\Users\\dell\\OneDrive\\Desktop\\Coding challenges\\FIle_Handling\\Copy.txt'

            if user_choice == 1:
                write_file(filename)
            elif user_choice == 2:
                read_file(filename)
            elif user_choice == 3:
                append_file(filename)
            elif user_choice == 4:
                print("Thanks for using the program...😁")
                break  # Exit the program
            else:
                print('Invalid choice, please enter a valid option (1-4).')
            print(' ')

    except Exception as e:
        print(f"An error occurred: {e}")

main()
