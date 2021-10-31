#!/usr/bin/env python3
"""
Módulo auxiliar para o contexto de conexão e comunicação com o firebase dentro da aplicação
"""

from main import user_option
import pyrebase
import os
from dotenv import load_dotenv
import json

load_dotenv()

firebaseConfig = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "projectId": os.getenv("PROJECT_ID"),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "databaseURL": os.getenv("DATABASE_URL"),
}


def connect():
    """
    Método responsável por criar o contexto de conexão e comunicação com o firebase.
    """
    return pyrebase.initialize_app(firebaseConfig)


def connect_auth(ctx):
    """
    Método de autenticação da aplicação com o firebase usando as credenciais de configuração.
    Retorna um contexto autenticado para manipulação de usuários.
    """
    return ctx.auth()


def connect_db(ctx):
    """
    Método de conexão da aplicação com os dados dentro do firebase.
    """
    return ctx.database()


def create_account(context, username, password):
    """
    Método de criação de usuário dentro do firebase.
    """
    context.create_user_with_email_and_password(username, password)
    print('Conta criada, favor confirmar o email na aplicação, dentro do menu "2".')


def get_info(context_auth, token, username):
    """
    Método que retorna as informações se o usuário existe ou não dentro do firebase.
    """
    return next(
        (
            u
            for u in context_auth.get_account_info(token)["users"]
            if u["email"] == username
        ),
        {"None": "False"},
    )


def sign_in(context, username, password):
    """
    Método que realiza login na aplicação, validando se o mesmo possui email confirmado.
    """
    status = context.sign_in_with_email_and_password(username, password)
    user = get_info(context, status["idToken"], username)
    if user.get("emailVerified", False):
        return (True, status)
    else:
        verify_email_token(context, status["idToken"])
        print("Email de confirmação enviado.")
        return (False, status)


def verify_email_token(context, user_id):
    """
    Método que realiza o envio de email de confirmação para o usuário
    """
    context.send_email_verification(user_id)
