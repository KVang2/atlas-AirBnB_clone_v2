#!/usr/bin/python3
"""
Using storage to fetch data from storage engine
Load all cities of state
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Use to remove SQLAlchemy session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    sorting = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorting)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
