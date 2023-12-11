#!/usr/bin/python3
""" start flask web app """

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Define a route for the root path """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Define a route for the root path "/hbnb" """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Returns string of a web server """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
def python_text(text):
    """ Returns string of web server """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """ display a number only if is an integer """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Display a HTML page if n is an int """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ Display a HTML page if n is an int odd or even """
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    """ Run the application on 0.0.0.0, port 5000 """
    app.run(host='0.0.0.0', port=5000)
