from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    recaptcha= RecaptchaField()

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is already taken. Please choose another one.")

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data.lower()).first()
        if user:
            raise ValidationError("That email is already taken. Please choose another one.")

class LoginForm(FlaskForm):
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateProfileForm(FlaskForm):
    username = StringField('Username',
                validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    submit = SubmitField('Update')
    profile_pic = FileField('Update profile picture',validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

    def validate_username(self,username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That username is already taken. Please choose another one.")

    def validate_email(self,email):
        if email.data != current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is already taken. Please choose another one.")


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no account with that email. You must register first.")


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
