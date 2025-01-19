import shutil

copy = ' '# Enter a name for the new copied file
shutil.copyfile('Copy.txt', copy) # Make a copy of the contents of a file
shutil.copy2('Copy.txt', copy) # Copy the metadata from a file
shutil.copy('Copy.txt', copy) # Copy file + permission mode + destination of the directory