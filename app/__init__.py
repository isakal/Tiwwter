import sys
import os
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
        print("Couldn't find key, exiting the program... \n")
        sys.exit(1)


app = Flask(__name__)
app.config.from_json('../keys.json')
app.config['MAIL_USERNAME'] = os.environ['TIWWTER_MAIL']
app.config['MAIL_PASSWORD'] = os.environ['TIWWTER_PASSWORD']

keys = getJSON("keys.json")

db = SQLAlchemy()

bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

from app.users.routes import users
from app.posts.routes import posts
from app.main.routes import main
from app.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)

def create_app(json_path="../keys.json"):
    app = Flask(__name__)
    app.config.from_json(json_path)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.users.routes import users
    from app.posts.routes import posts
    from app.main.routes import main
    from app.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
