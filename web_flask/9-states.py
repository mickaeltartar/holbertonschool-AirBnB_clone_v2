#!/usr/bin/python3
""" Script that starts a Flask web application and display
a HTML page with list ID of a state """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state_no_ID():
    """ define a root for the root path for states without ID """
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_ID(id):
    """ define a root for the root path for states with ID  """
    states = storage.all(State)
    state_ID = "State." + id if id else None
    return render_template('9-states.html', states=states, state_ID=state_ID)


@app.teardown_appcontext
def close_DB(self):
    """ close DB after request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
