#!/usr/bin/python3
"""
Fetching data from storage engine,
removing current SQLAlchemy session after each request
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


def close_session(exception):
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
