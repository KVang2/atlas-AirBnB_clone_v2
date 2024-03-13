#!/usr/bin/python3
"""
Using storage to fetch data from storage engine
Load all cities of state
Remove current SQLAlchemy session, declare method to handle @app
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Use to remove SQLAlchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def state_s():
    states = sorted(list(storage.all(Stage). values()), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', no_html=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
