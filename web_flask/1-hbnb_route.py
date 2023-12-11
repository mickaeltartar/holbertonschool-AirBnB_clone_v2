#!/usr/bin/python3

""" start flask web app """

from flask import Flask
app = Flask(__name__)


#!/usr/bin/python3

""" start flask web app """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Define a route for the root path "/" """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Define a route for the root path "/hbnb" """
    return 'HBNB'

if __name__ == '__main__':
    """ Run the application on 0.0.0.0, port 5000 """
    app.run(host='0.0.0.0', port=5000)
