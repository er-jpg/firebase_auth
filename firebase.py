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
    return pyrebase.initialize_app(firebaseConfig)


def connect_auth(ctx):
    return ctx.auth()


def connect_db(ctx):
    return ctx.database()


def create_account(context, username, password):
    context.create_user_with_email_and_password(username, password)


def get_info(context_auth, token, username):
    return next(
        (
            u
            for u in context_auth.get_account_info(token)["users"]
            if u["email"] == username
        ),
        {"None": "False"},
    )


def sign_in(context, username, password):
    status = context.sign_in_with_email_and_password(username, password)
    user = get_info(context, status["idToken"], username)
    if user.get("emailVerified", False):
        return (True, status)
    else:
        verify_email_token(context, status["idToken"])
        print("Email de confirmação enviado.")
        return (False, status)


def verify_email_token(context, user_id):
    context.send_email_verification(user_id)
