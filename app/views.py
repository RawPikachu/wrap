from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_user")
def add_user():
    return render_template("add_user.html")
