import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


def getJSON(filename):
    with open(filename,'r') as fp:
        return json.load(fp)


keys = getJSON("keys.json")
appSecretKey = keys.get("app_secret_key")
recaptcha_keys = keys['recaptcha_keys']
recaptchaKeyPublic = recaptcha_keys['public']
recaptchaKeyPrivate = recaptcha_keys['private']

app = Flask(__name__)
app.config['SECRET_KEY'] = appSecretKey
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['RECAPTCHA_PUBLIC_KEY'] = recaptchaKeyPublic
app.config['RECAPTCHA_PRIVATE_KEY'] = recaptchaKeyPrivate

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from app import routes
