from flask import render_template, url_for, flash, redirect, request
from website import app, db, bcrypt
from website.forms import RegistrationForm, LoginForm, UpdateProfile
from website.models import User, Post
from flask_login import login_user, current_user, logout_user,login_required


posts = [

    {
        "author": "saki",
        "title": "Post 1",
        "content": "Trying stuff out",
        "date_posted": "January 20, 2018"
    },
    {
        "author": "spinzed",
        "title": "Post 2",
        "content": "boi",
        "date_posted": "January 24, 2018"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. Please login.','success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account/")
@app.route("/account")
@login_required
def account():
    image_file = url_for('static',filename='profile_pics/{}'.format(current_user.image_file))
    return render_template('account.html',title='Your account',image_file=image_file)


@app.route("/account/edit/", methods=['GET', 'POST'])
@app.route("/account/edit", methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been successfully updated !','success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename='profile_pics/{}'.format(current_user.image_file))
    return render_template('edit_profile.html',title='Your account',image_file=image_file,form=form)



@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
