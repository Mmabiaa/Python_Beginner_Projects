# Checking if a file or directory is present
import os

path = 'C:\\Users\\dell\OneDrive\\Desktop\\Coding challenges\\FIle_Handling\\Copy.txt' # Enter the path to the file or directory

if os.path.exists(path):

    if os.path.isdir(path):
        print("Directory was found!")
    elif os.path.isfile(path):
        print('File was found')
else:
    print('File or directory not found!')