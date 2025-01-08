import requests
import schedule
import time

phone_number = '+233599670295'  # Enter the number you're sending the message to.

def send_message():
    # Corrected the URL typo here
    resp = requests.post('http://textbelt.com/text', {
        'phone': phone_number, 
        'message': 'Hello, world',
        'key': 'textbelt'  # Replace with your own API key if needed
    })

    # Print the response from the Textbelt API
    print(resp.json())

# Schedule the task to run every day at 6pm
schedule.every().day.at('00:10').do(send_message)

# Keep the script running and check the schedule
while True:
    schedule.run_pending()
    time.sleep(60)  # Check the schedule every minute
