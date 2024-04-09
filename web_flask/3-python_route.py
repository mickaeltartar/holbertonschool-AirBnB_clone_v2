#!/usr/bin/python3
""" start flask web appli """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ define a root for the root path """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ define a second root for the root path """
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """ replace text """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
def python_is_cool(text):
    """ replace text & display "is cool" """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
