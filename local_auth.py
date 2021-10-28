import random
import email_sender


def send_email_confirmation(user, user_code):
    email_sender.send_email(user, user_code)


def validate(user):
    random_code = random.randint(1000, 9999)
    send_email_confirmation(user, random_code)

    user_input = input("Favor digitar o código enviado no email: ")

    if user_input == random_code or int(user_input) == random_code:
        print("Bem-vindo à aplicação")
    else:
        print("Código invalido.")
