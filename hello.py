"""Modules"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     """Hello world"""
#     return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello_name(name):
    """Hello name"""
    return f"Hello, {escape(name)}!"

@app.route('/')
def index():
    """Index route"""
    return 'Index Page'

@app.route('/hello')
def hello():
    """Hello world route"""
    return 'Hello, World'
