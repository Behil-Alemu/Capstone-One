from turtle import title
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
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
    