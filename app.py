from email.mime import image
from tkinter import Image
from urllib import response
from flask import Flask, request, render_template,  redirect, flash, session, g
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, User, Post,Likes,Inspiration
from sqlalchemy.exc import IntegrityError,InvalidRequestError
from form import UserAddForm, LoginForm, UserEditForm, PostForm
import json
import requests
from random import sample

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///capstone_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)



connect_db(app)
# db.create_all()

API_BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1 "



# for i in range(len.lenghtofAPI)
# api url with object id randrange(length) random.sample
# val = random.choices(array of list, k=10) print(val)

##############################################################################
# search
search_base_api = "https://collectionapi.metmuseum.org/public/collection/v1/search"
objectIDs_api="https://collectionapi.metmuseum.org/public/collection/v1/objects/"

@app.route('/')
def homepage():
    """Show homepage:"""
    search = str(request.args.get('image'))
    res = requests.get(f"{search_base_api}",params={"q":search, "hasImages": "true"})
    data = res.json()
   
    ten_random = sample(list(data['objectIDs']), 10)
    print(ten_random)

    
    data_url= data["objectIDs"][0]
  
    object_res = requests.get(f"{objectIDs_api}{data_url}")
    object_data=object_res.json()
    image_url= object_data["primaryImage"]


    return render_template('home/home.html', image=image_url)





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
    If the there already is a user with that username: flash message and re-present form.
    """

    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
                avatar=form.avatar.data or User.avatar.default.arg)
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

@app.route('/post/new', methods=["GET", "POST"])
def messages_add():
    """Add a post:

    Show form if GET. If valid, update message and redirect to user page.
    """

    if not g.user:
        flash("Please sign up first : }", "info")
        return redirect("/")

    form = PostForm()

    if form.validate_on_submit():
        post = Post(title=form.title.data, 
                    description=form.description.data,
                    imageURL=form.imageURL.data)
        g.user.posts.append(post)
        db.session.commit()
        return redirect("/posts")
    return render_template('posts/addpost.html', form=form)

@app.route('/posts/user', methods=["GET"])
def show_posts():
    """Show a message."""
    if g.user:
        post = (Post.query.order_by(Post.created_at.desc()).limit(15).all())
        likes= [post.id for post in g.user.likes]
        return render_template('posts/show.html', post=post, likes=likes)
    else:
        return render_template('home/home-anon.html')

##############################################################################
#  users pofile:
@app.route('/users/<int:user_id>')
def users_show(user_id):
    """Show user profile."""

    user = User.query.get_or_404(user_id)

    return render_template('users/show.html', user=user)

@app.route('/users/profile', methods=["GET", "POST"])
def profile():
    """Update profile for current user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect(f"/users/{g.user.id}")

    user=g.user
    form = UserEditForm()

    if form.validate_on_submit():
        try:
            if User.authenticate(user.username,form.password.data):
                user.email=form.email.data
                user.image_url=form.image_url.data or User.image_url.default.arg
                user.bio=form.bio.data
                user.location=form.location.data
                user.header_image_url=form.header_image_url.data

                db.session.commit()
        except IntegrityError:
            flash("Wrong password", 'danger')
            return render_template('users/edit.html', form=form)
        except InvalidRequestError:
            flash("Email taken", 'danger')
            return render_template('users/edit.html', form=form)
        #  why does this not work?

        return redirect(f"/users/{user.id}")

    else:
        return render_template('users/edit.html', form=form, user=user)


@app.route('/users/delete', methods=["POST"])
def delete_user():
    """Delete user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    do_logout()

    db.session.delete(g.user)
    db.session.commit()

    return redirect("/signup")