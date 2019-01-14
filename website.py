from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello():
	return "<h1>pizza OG</h1>"


@app.route("/pizza")
def pizza():
	return "<h2>pizza pizza</h2>"


if __name__ == '__main__':
	app.run(debug=True)
