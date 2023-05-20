"""
Routes for this flask blog
"""

from flask import flash, redirect, render_template, url_for

from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    """Routes for the home page"""
    user = {"username": "Stephen"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    """A login route for handling get/put request to login"""
    form = LoginForm()
    # If the form is valid, redirect to home
    if form.validate_on_submit():
        flash(
            f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}"
        )
        return redirect(url_for("index"))
    # If the form is not valid, render the login template
    return render_template("login.html", title="Sign In", form=form)
