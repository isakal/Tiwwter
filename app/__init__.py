import sys
import os
import json
from flask import Flask
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy()

bcrypt = Bcrypt()

toolbar = DebugToolbarExtension()

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

def create_app():
	app = Flask(__name__)
	app.config.from_object(ProductionConfig if os.environ['TIWWTER_PROD'] == 'True' else DevelopmentConfig)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)
	toolbar.init_app(app)

	from app.users.routes import users
	from app.posts.routes import posts
	from app.main.routes import main
	from app.errors.handlers import errors

	app.register_blueprint(users)
	app.register_blueprint(posts)
	app.register_blueprint(main)
	app.register_blueprint(errors)

	return app
