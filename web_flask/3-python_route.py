#!/usr/bin/python3
"""
Flask web application
containing routes
'/', '/hbnb', '/c/<text>, '/python/<text>'
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return "C " + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
