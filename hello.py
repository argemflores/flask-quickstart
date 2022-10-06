"""Modules"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Hello world"""
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    """Hello name"""
    return f"Hello, {escape(name)}!"
