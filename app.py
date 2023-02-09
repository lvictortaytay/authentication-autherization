from contextlib import redirect_stderr
from functools import reduce
from flask import Flask, redirect, render_template , flash , session
from models import connect_db , db , User , bcrypt
from forms import register , loginform


app = Flask(__name__)
connect_db(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///users"
app.config["SECRET_KEY"] = "hjbhsbdcs"

@app.route("/")
def home_page():
    session["username"] = "none"
    return render_template("home.html")



@app.route("/login" , methods = ["POST" , "GET"])
def login_page():
    form = loginform()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        User.authenticate(username = username , pwd = password)
        flash("login succesful" , "success")
        session["username"] = f"{username}"
        return redirect("/secret")
    else:
        return render_template("login.html" , form = form)





@app.route("/register" , methods = ["GET" , "POST"])
def signup_page():
    form = register()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        User.register(username = username , pwd = password)
        session["username"] = f"{username}"
        return redirect("/secret")
    else:
        return render_template("signup.html" , form = form)


@app.route("/secret")
def secret_page():
    if session["username"] != "none":
        return render_template("secret.html")
    else:
        flash("must login to view content!" , "error")
        return redirect("/login")
