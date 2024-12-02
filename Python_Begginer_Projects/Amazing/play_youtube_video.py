import pywhatkit
try:

    Song = input("Enter Song Name: ")
    pywhatkit.playonyt (Song)
    print("Successfully Played!")

except:
    print("An Unexpected Error!")