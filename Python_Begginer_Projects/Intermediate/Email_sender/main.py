from email.message import EmailMessage # A library that provides email methods
import ssl # A library that helps to send message
import smtplib
from variables import password # Importing stored variables.

def Email_Details():
    sender_email = input('Please enter your email address: ').strip().lower()

    email_password = password

    receiver_email = input('Please enter the recipient email address: ').strip().lower()

    subject = input('Enter the email subject: ')

    body = input("Enter your email message: \n")

    return sender_email, receiver_email, email_password, subject, body


def send_email(sender_email, receiver_email, subject, body):
    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(body)

    return em

def Login(sender_email, receiver_email, email_password, em):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, email_password)
        smtp.sendmail(sender_email, receiver_email, em.as_string())

def Main():
    sender_email, receiver_email, email_password, subject, body = Email_Details()
    em = send_email(sender_email, receiver_email, subject, body)
    Login(sender_email, receiver_email, email_password, em)
    print(" ")
    print('Email sent successfully!')

Main()