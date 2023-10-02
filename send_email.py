import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = "pawan2004soni@gmail.com"
    pwd = os.getenv("PASSWORD")

    receiver = "pawan2004soni@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context)as server:
        server.login(user_name, pwd)
        server.sendmail(user_name, receiver, message)