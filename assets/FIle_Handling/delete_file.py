import os
import shutil

path = 'C:\\Users\\dell\\OneDrive\\Desktop\\Coding challenges\\FIle_Handling\\Copy.txt' # Path to file to be deleted

dir = 'C:\\Users\\dell\\OneDrive\\Desktop\\Coding challenges\\FIle_Handling\\Empty_folder' # Directory to be deleted

folder = 'C:\\Users\\dell\\OneDrive\\Desktop\\Coding challenges\\Folder' # File containing folder to be deleted

try: # Try block to check errors

    os.remove(path) # Function to delete file
    os.rmdir(dir) # Function to delete directory or empty folder

    shutil.rmtree(folder) # Function to delete Folder containing a file


except PermissionError: # Check for permission error
    print("You do not have permission to delete this!")

except FileNotFoundError: # Check for file not found
    print("FIle was not file")

except OSError: # Check for directory not found
    print("YOu cannot delete that using that function")

else: # Statement for success
    print('File/Directory was deleted successfully')