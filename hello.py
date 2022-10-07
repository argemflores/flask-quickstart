"""Modules"""
from flask import Flask, url_for, request, render_template, make_response, abort, redirect, session
from markupsafe import escape
from werkzeug.utils import secure_filename
from pandas import DataFrame

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

# @app.route('/')
# def index():
#     """Index"""
#     return 'index'

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

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     """Login

#     Returns:
#         None: Print login message
#     """
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])

#         error = 'Invalid username/password'
#     else:
#         error = 'View only'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

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

# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))
#     print(url_for('static', filename='style.css'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """Upload a file
    """
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")

@app.route('/cookies')
def test_cookies():
    """Cookies
    """
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.

    print(username)

    resp = make_response(render_template('hello.html'))
    resp.set_cookie('username', 'the username')

    return resp

# @app.route('/')
# def index():
#     """Redirect

#     Returns:
#         None: Redirect page
#     """
#     return redirect(url_for('abort_page'))

def this_is_never_executed():
    """Print error
    """
    print("ERROR!")

@app.route('/abort_page')
def abort_page():
    """Abort page
    """
    abort(401)
    this_is_never_executed()

@app.errorhandler(404)
def page_not_found(error):
    """Show page not found error

    Args:
        error (str): Error message

    Returns:
        str: Page not found page
    """
    return render_template('page_not_found.html', error=error), 404

@app.errorhandler(404)
def not_found(error):
    """Response not found error object

    Args:
        error (str): Error message

    Returns:
        Response: Response object
    """
    resp = make_response(render_template('error.html', error=error), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

@app.route("/me")
def me_api():
    """Return a JSON response

    Returns:
        dict: User description
    """
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        # "image": url_for("user_image", filename=user.image),
        "image": user.image
    }

def get_current_user():
    """Get user

    Returns:
        dict: One user
    """
    return get_all_users().iloc[0]

def get_all_users():
    """Get all users

    Returns:
        list: All users
    """
    data = {'username': ['usr1', 'usr2'], 'theme': ['thm1', 'thm2'], 'image': ['img1', 'img2']}
    data_frame = DataFrame(data=data)
    return data_frame

@app.route("/users")
def users_api():
    """Return list of users

    Returns:
        dict: List of users
    """
    users = get_all_users()
    return [user.to_json() for user in users]

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    """Index page for session

    Returns:
        str: Message
    """
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login

    Returns:
        str: Form
    """
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    """Log out

    Returns:
        str: Redirect page
    """
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
