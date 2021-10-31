#!/usr/bin/env python3
"""
Módulo auxiliar para a autorização em dois fatores após verificação de email e para login na aplicação
"""

import random
import email_sender


def send_email_confirmation(user, user_code):
    """
    Método de envio de email de confirmação de usuário
    """
    email_sender.send_email(user, user_code)


def validate(user):
    """
    Método de validação de usuário em dois fatores, que envia o email e valida o código recebido pelo usuário na tela
    """
    random_code = random.randint(1000, 9999)
    send_email_confirmation(user, random_code)

    user_input = input("Favor digitar o código enviado no email: ")

    if user_input == random_code or int(user_input) == random_code:
        print("Bem-vindo à aplicação")
    else:
        print("Código invalido.")
