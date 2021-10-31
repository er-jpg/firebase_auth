#!/usr/bin/env python3
"""
Módulo auxiliar para a autorização em dois fatores após verificação de email e para login na aplicação
"""

import random
import email_sender
from os import path, stat, chmod
from stat import *
from datetime import datetime
import pathlib


def send_email_confirmation(email, user_code):
    """
    Método de envio de email de confirmação de usuário
    """
    email_sender.send_email(email, user_code)


def validate(email):
    """
    Método de validação de usuário em dois fatores, que envia o email e valida o código recebido pelo usuário na tela
    """
    random_code = random.randint(1000, 9999)
    send_email_confirmation(email, random_code)

    user_input = input("Favor digitar o código enviado no email: ")

    if user_input == random_code or int(user_input) == random_code:
        register_login_file(email)
        print("Bem-vindo à aplicação")
    else:
        print("Código invalido.")


def register_login_file(email):
    """
    Método que realiza a leitura e a escrita do log de login por usuários dentro da aplicação, com o nome de acesso.txt e com mudanças de permissões do arquivo.
    Utiliza a hora da BIOS/UEFI.
    """
    file_name = "acesso.txt"
    if path.isfile(file_name):
        mode = stat(file_name).st_mode

        if mode != S_IRWXU:  # S_IRWXU is the code for ownership of a file
            file_path = pathlib.Path(file_name)
            chmod(file_path, S_IRWXU)
        f = open(file_name, "a")
    else:
        f = open(file_name, "w")

    now = datetime.now()
    row_data = "Email: " + email + "\tData-hora: " + str(now) + ".\n"
    f.write(row_data)
    f.close()

    chmod(file_name, S_IRUSR)
