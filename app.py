from email.mime import image
from flask import Flask, request, render_template,  redirect, flash, session, g
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, User, Post,Likes,Inspiration
from sqlalchemy.exc import IntegrityError,InvalidRequestError
from forms import UserAddForm, LoginForm, MessageForm, UserEditForm, PostForm
import json
import requests

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///capstone_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)



connect_db(app)
db.create_all()

API_BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1 "

# def search_art(searched):
#     res = requests.get(f"{API_BASE_URL}/search?hasImages=true&q=Paintings&p={searched}")
#     data = res.json()
#     image= data["objectIDs"][0]["primaryImage"]
#     return image

# @app.route('/')
# def show_search_form():
#     return render_template("base.html")


# @app.route('/show_searched_art')
# def get_art():
#     searched = request.args["image"]
#     image_url = search_art(searched)
#     # import pdb; pdb.set_trace()
#     return render_template('base.html', image_url=image_url)

# for i in range(len.lenghtofAPI)
# api url with object id randrange(length)


response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&q=Paintings&p=African")
data = response.json()
url = data["objectIDs"][0]



# res_id = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/{url}")

# data_url = res_id.json()
# image_URL= data_url["primaryImage"]

def search_art(searched):
    res = requests.get(f"{API_BASE_URL}/search?hasImages=true&q=Paintings&p={searched}")
    # data_url = res.json()
    primaryImage= res["primaryImage"]
    image = {'primaryImage': primaryImage}
    return image

search_art(url)


##############################################################################
# User signup/login/logout

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None
# I do not understand flask global all to well

def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """

    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
                Avatar=form.image_url.data or User.image_url.default.arg)
            db.session.commit()
        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    session.pop(CURR_USER_KEY)
    # or do_logout()
    flash("Goodbye!", "info")
    return redirect('/login')

##############################################################################
# list users post:
@app.route('/users-post/<int:user_id>')
def users_show(user_id):
    """Show user profile."""

    user = User.query.get_or_404(user_id)
    # snagging messages in order from the database;
    # user.messages won't be in order by default
    post = (Post
                .query
                .filter(Post.user_id == user_id)
                .order_by(Post.timestamp.desc())
                .limit(10)
                .all())
    likes= [msg.id for msg in user.likes]

    return render_template('users/show.html', user=user, post=post, likes=likes)