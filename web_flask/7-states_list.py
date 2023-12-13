#!/usr/bin/python3
"""
Script that starts a Flask web application and display
a HTML page with list of states sorted by name
"""

from flask import Flask
from models import storage
from models.state import State
from flask import render_template

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of states sorted by name"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def closeDB(self):
    """ Close the database after request """
    storage.close()

if __name__ == "__main__":
    """ Run the application on 0.0.0.0, port 5000 """
    app.run(host='0.0.0.0', port=5000)