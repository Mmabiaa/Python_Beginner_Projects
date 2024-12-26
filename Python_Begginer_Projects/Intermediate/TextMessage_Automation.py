import requests
import schedule
import time

phone_number = '' # Enter the number you're sending the message to. 

def send_message():
    resp = requests.post('http;//textbelt.com/text', {
    'phone': phone_number, 
    'message': 'Hello, world',
    'key': 'textbelt'
    })

    print(resp.json())
# Schedule at 6pm everyday.
schedule.every().day.at('18:00').do(send_message)

# Author - Mmabiaa
