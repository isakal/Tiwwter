from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '47e2d772b1ae98f3ad199dd2e1793757'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfJTpIUAAAAAB8eRPVrytaqFACnMM87AUDqU0MG'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfJTpIUAAAAABndeU9uz5aHtFBoZkRNK_jySbNP'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from website import routes
