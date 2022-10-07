"""Modules"""
from flask import Flask, url_for, request, render_template
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

# @app.route('/hello')
# def hello():
#     """Hello world route"""
#     return 'Hello, World'

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

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     """Login using GET and POST"""
#     if request.method == 'POST':
#         return do_the_login()

#     return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    """User profile"""
    return f'{username}\'s profile'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    """Render hello.html template

    Args:
        name (string, optional): Any name or value. Defaults to None.

    Returns:
        None: Print hello.html contents
    """
    return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    """Login

    Returns:
        None: Print login message
    """
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])

        error = 'Invalid username/password'
    else:
        error = 'View only'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

def valid_login(username, password):
    """Validate login

    Args:
        username (str): Username
        password (str): Password

    Returns:
        bool: True if valid; False otherwise
    """
    return username and password

def log_the_user_in(username):
    """Show login message

    Args:
        username (str): Username

    Returns:
        None: Print login message
    """
    return f'{username} logged in!'

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('static', filename='style.css'))
