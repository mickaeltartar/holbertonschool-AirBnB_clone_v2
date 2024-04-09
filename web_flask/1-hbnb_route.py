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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
