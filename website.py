from flask import Flask, render_template,url_for

app = Flask(__name__)

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


if __name__ == '__main__':
	app.run(debug=True)
