#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
def index():
	return 'Hello HBNB!'

if __name == '__main__':
	app.run(host='0.0.0.0', port=5000)
