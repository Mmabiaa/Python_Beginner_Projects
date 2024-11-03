# A simple program that splits emails into username, domain, and extension

def Email(): # A function that holds email  addresses and split them into username, domain, and extension.
    print("Welcome to Email_Slicer")
    print('')
    while True:
        try:
            email = input("Enter your email address: ").lower().strip()
            (username, domain) = email.split('@') # Split before and after '@'
            (domain, extension) = domain.split('.') # Split before and after '.'

            # Display various results
            print(f"Your username is: {username}")
            print(f"Your domain is: {domain}")
            print(f"Your extension is: {extension}")

        except: # Error handling
            print("Invalid email address.")
            continue
        break

def Main():
    while True:

        Email()

        choice = input("Do you want to continue? (y/n): ")

        if choice == 'y':
            continue
        else:
            print('Thanks for using the program...😁')
            break
    
Main()

