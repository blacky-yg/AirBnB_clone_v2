#!/usr/bin/python3
"""Flask application 2 routes"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """Displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(c_text):
    """Displays C"""
    return 'C %s' % c_text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def display_python(py_text='is cool'):
    """Displays Python"""
    return 'Python %s' % py_text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
