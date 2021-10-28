#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Bruno Saragosa da Silva"
__version__ = "0.1.0"

import firebase
import local_auth


def main():
    ctx = firebase.connect()
    auth = firebase.connect_auth(ctx)

    user_option(auth)


def user_option(context_auth):
    opt = input(
        "Digite 1 para cadastro de usuário, 2 para confirmação de email e 3 para autenticação: "
    )

    user = input("Digite seu e-mail: ")
    password = input("Digite sua senha, com pelo menos 6 caracteres: ")

    if opt == "1":
        firebase.create_account(context_auth, user, password)
    elif opt == "2":
        firebase.sign_in(context_auth, user, password)
    elif opt == "3":
        firebase.sign_in(context_auth, user, password)
        local_auth.validate(user)
    else:
        print("Favor selecionar valor.")


if __name__ == "__main__":
    main()
