from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField


class register(FlaskForm):
    
    username = StringField("username")
    password = PasswordField("password")
    email = StringField("email")
    first_name = StringField("first name")
    last_name = StringField("last name")



class loginform(FlaskForm):

    username = StringField("username")
    password = PasswordField("password")
    