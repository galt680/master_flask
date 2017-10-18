from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,StringField, FileField

class LoginForm(FlaskForm):
    username = StringField(' Enter username',)
    password = PasswordField('Enter password',)

class UploadForm(FlaskForm):
    file = FileField()