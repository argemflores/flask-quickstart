"""Modules"""
from flask import Flask, url_for, request
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

# @app.route('/')
# def index():
#     """Index route"""
#     return 'Index Page'

@app.route('/hello')
def hello():
    """Hello world route"""
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    """Show the user profile for that user"""
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    """Show the post with the given id, the id is an integer"""
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    """Show the subpath after /path/"""
    return f'Subpath {escape(subpath)}'

@app.route('/')
def index():
    """Index"""
    return 'index'

def do_the_login():
    """Do the login"""
    return 'do the login'

def show_the_login_form():
    """Show the login form"""
    return 'show the login form'

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login using GET and POST"""
    if request.method == 'POST':
        return do_the_login()

    return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    """User profile"""
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
