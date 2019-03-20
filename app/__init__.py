import sys
import json
from flask import Flask
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


def getJSON(filename):
    try:
        with open(filename,'r') as fp:
            return json.load(fp)
    except FileNotFoundError:
        print("Couldn't find key, exiting the program...")
        sys.exit(1)


keys = getJSON("keys.json")
appSecretKey = keys.get("app_secret_key")
recaptcha_keys = keys['recaptcha_keys']
recaptchaKeyPublic = recaptcha_keys['public']
recaptchaKeyPrivate = recaptcha_keys['private']
MAIL_EMAIL = keys.get("mail_email")
MAIL_PASSWORD = keys.get("mail_password")

app = Flask(__name__)
app.config['SECRET_KEY'] = appSecretKey
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['RECAPTCHA_PUBLIC_KEY'] = recaptchaKeyPublic
app.config['RECAPTCHA_PRIVATE_KEY'] = recaptchaKeyPrivate
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = MAIL_EMAIL
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

mail = Mail(app)

from app import routes
