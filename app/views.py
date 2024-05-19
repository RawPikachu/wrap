from app import app
from flask import render_template, request


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")
    if request.method == "POST":
        print(request.form)
        return "User added successfully!"
