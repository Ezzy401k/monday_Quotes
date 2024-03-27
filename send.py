import datetime as dt
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

my_email = input("Email: ")
password = input("Password: ")
receiver = input("Receiver Email: ")
now = dt.datetime.now()
date = now.weekday()

if date == 0:
    with open("quotes.txt") as file:
        quote = file.readlines()

    quote_list = [text.strip() for text in quote]

    one_quote = random.choice(quote_list)

    message = MIMEMultipart()
    message["From"] = my_email
    message["To"] = receiver
    message["Subject"] = "Quote of the day"

    body = one_quote
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        # Log in to the account
        server.login(my_email, password)
        # Send the email
        server.sendmail(my_email, receiver, message.as_string())
