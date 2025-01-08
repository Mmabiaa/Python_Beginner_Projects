from email.message import EmailMessage # A library that provides email methods
import ssl # A library that helps to send message
import smtplib # A library that helps to login into your email
from variables import password # Importing stored variables.

def Email_Data(): # A function to return email details
    sender_email = input('Please enter your email address: ').strip().lower()

    email_password = password

    receiver_email = input('Please enter the recipient email address: ').strip().lower()

    subject = input('Enter the email subject: ')

    body = input("Enter your email message: \n")

    return sender_email, receiver_email, email_password, subject, body


def Message_Data(sender_email, receiver_email, subject, body): # A function that use returned email details to send emails
    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(body)

    return em

def Login(sender_email, receiver_email, email_password, em): # A function that uses email details to login into the and send messages
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, email_password)
        smtp.sendmail(sender_email, receiver_email, em.as_string())

def Main(): # A main function that holds all the functions to be called
    sender_email, receiver_email, email_password, subject, body = Email_Data()
    em = Message_Data(sender_email, receiver_email, subject, body)
    Login(sender_email, receiver_email, email_password, em)
    print(" ")
    print('Email sent successfully!')

Main()