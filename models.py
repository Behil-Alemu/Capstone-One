"""Models for Metropolitan Museum of Art project."""
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import datetime

from requests import post

bcrypt = Bcrypt()
db = SQLAlchemy()


class User(db.Model):
    """Make a table with user info"""
    __tablename__='users'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    username = db.Column(db.Text,nullable=False,unique=True,)

    email = db.Column(db.Text,nullable=False,unique=True)

    avatar = db.Column(db.Text,nullable=False, default="https://tinyurl.com/demo-cupcake")

    social_media = db.Column(db.Text,nullable=True,)

    bio = db.Column(db.Text)

    password = db.Column(db.Text,nullable=False)
    
    posts = db.relationship('Post',backref='users')
    inspiration=db.relationship('Inspiration'
    )
    likes =db.relationship('Post',
        secondary="like"
    )

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"
    
    @classmethod
    def signup(cls, username, email, password, avatar):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            avatar=avatar,
        )

        db.session.add(user)
        return user


    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False




class Post(db.Model):
    """Post table """
    __tablename__='post'    

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.Text, nullable=False, unique=False)

    description= db.Column(db.Text, nullable=True, unique=False)

    imageURL = db.Column(db.Text,nullable=False,default="https://tinyurl.com/demo-cupcake")

    created_at=db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User')

    @property
    def friendly_date(self):
        """Makes the date look user friendly"""
        return self.created_at.strftime("%a %b %-d %Y, %-I:%M %p")

class Likes(db.Model):
    """Mapping of a Post to a Tag."""

    __tablename__ = "like"

    post_id = db.Column(db.Integer,db.ForeignKey("post.id", ondelete='cascade'),primary_key=True)

    user_id = db.Column(db.Integer,db.ForeignKey("users.id", ondelete='cascade'),primary_key=True)
    posts = db.relationship('Post',backref='like')
    user = db.relationship('User',backref='like')


class Inspiration(db.Model):
    """Make a table with user inspiration arts"""
    __tablename__='inspiration'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    inspiration = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"), primary_key=True)

    users = db.relationship('User',backref='inpiration')


def connect_db(app):
    db.app = app
    db.init_app(app)