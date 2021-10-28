import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("SMTP_SERVER")
port = os.getenv("SMTP_PORT")
username = os.getenv("SMTP_USERNAME")
password = os.getenv("SMTP_PASSWORD")


def send_email(mail_to, verification_code):
    mail_from = username
    mail_subject = "Segurança da Tecnologia da Informação"
    mail_body = "Seu código de verificação é: " + str(verification_code) + "."

    message = MIMEMultipart()
    message["From"] = mail_from
    message["To"] = mail_to
    message["Subject"] = mail_subject
    message.attach(MIMEText(mail_body, "plain"))

    connection = smtplib.SMTP(server, port)
    connection.starttls()
    connection.login(username, password)
    connection.send_message(message)
    connection.quit()
