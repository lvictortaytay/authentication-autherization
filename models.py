from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from forms import register

bcrypt = Bcrypt()
db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)



class User(db.Model):
    __tablename__ = "users"


    username = db.Column(db.String(20), primary_key = True , unique = True)

    password = db.Column(db.String, nullable = False)

    email = db.Column(db.String(50), unique = True , nullable = False)

    first_name = db.Column(db.String(30), nullable = False)
    
    last_name = db.Column(db.String(30), nullable = False)

    @classmethod
    def register(cls ,username ,pwd):
        """register user with hashed password and return user"""
        form = register()
        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode("utf8")
        new_user = cls(username = username  , password = hashed_utf8 , email = form.email.data , first_name = form.first_name.data , last_name = form.last_name.data)
        db.session.add(new_user)
        db.session.commit()

        return cls(username = username  , password = hashed_utf8)

    @classmethod
    def authenticate(cls, username, pwd):
        u = User.query.filter_by(username = username).first()

        if u and  bcrypt.check_password_hash(u.password , pwd):
            return u
        else:
            return False




