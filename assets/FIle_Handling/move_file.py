import os

source = 'Copy.txt '
destination = 'C:\\Users\\dell\\OneDrive\\Desktop\\Coding challenges\\FIle_Handling\\Copy.txt'

try:
    if os.path.exists(destination):
        print("There is already a file")
        
    else:
        os.replace(source, destination)
        print(source + 'was moved to' + destination)


except FileNotFoundError:
    print(source + ' does not exist!')
