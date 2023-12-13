#!/usr/bin/python3
"""
Script that starts a Flask web application and display
a HTML page with list of states sorted by name
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of states sorted by name"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_db(self):
    """Closes the database after a request has been processed"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
