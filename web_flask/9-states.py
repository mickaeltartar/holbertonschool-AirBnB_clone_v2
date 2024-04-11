#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_no_id():
    """Display a list of all State objects"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Researsh states with id"""
    states = storage.all(State)
    state_id = 'State.' + id if id else None
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the database after process"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
