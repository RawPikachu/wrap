from app import app
from models import User
from flask import render_template, request

users = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")

    if request.method == "POST":
        choices = []

        for item in request.form.keys():
            if item != "name":
                choices.append(item)

        if request.form.get("name", False):
            return render_template("add_user.html", error="Name cannot be empty")

        user = User(request.form["name"], choices)
        user.calculate_stats()
        users.append(user)

        return render_template("index.html")
