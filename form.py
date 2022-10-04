from turtle import title
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField,SelectField
from wtforms.validators import DataRequired, Email, Length


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    avatar = SelectField('Avatar', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])

class UserEditForm(FlaskForm):
    """Form for editing profile"""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    avatar = SelectField('Avatar', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    social_media = StringField('(Optional) Social Media @')
    bio=StringField('(Optional) Bio')



class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class PostForm(FlaskForm):
    """Post form."""

    title = StringField('Title:', validators=[DataRequired()])
    description = StringField('Description:', validators=[DataRequired()])
    imageURL = StringField('Your Art URL:', validators=[DataRequired()])

class EditPostForm(FlaskForm):
    """Post form."""

    title = StringField('Title:', validators=[DataRequired()])
    description = StringField('Description:', validators=[DataRequired()])
    imageURL = StringField('Your Art URL:', validators=[DataRequired()])

choices={
    1: "American Decorative Arts", 
    3: "Ancient Near Eastern Art",
    4: "Arms and Armor",
    5: "Arts of Africa, Oceania, and the Americas",
    6: "Asian Art",
    7: "The Cloisters",
    8: "The Costume Institute",
    9: "Drawings and Prints",
    10: "Egyptian Art",
    11: "European Paintings",
    12: "European Sculpture and Decorative Arts",
    13: "Greek and Roman Art",
    14: "Islamic Art",
    15: "The Robert Lehman Collection",
    16: "The Libraries",
    17: "Medieval Art",
    18: "Musical Instruments",
    19: "Photographs",
    21: "Modern Art"
}


 