from flask import Flask, render_template,url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = open("SECRET_KEY.txt","r")

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
	return render_template("home.html",posts=posts,title=None)


@app.route("/about")
def about():
	return render_template("about.html",title="About")

@app.route("/register")
def register():
	form=RegistrationForm()
	return render_template("registration.html",title="Register",form=form)

app.route("/login")
def login():
	form=LoginForm()
	return render_template("login.html",title="Login",form=form)


if __name__ == '__main__':
	app.run(debug=True)

	#12:19 pt3
