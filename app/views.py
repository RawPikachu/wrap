from app import app
from models import User
from flask import render_template, redirect, url_for, request
from PIL import Image, ImageDraw, ImageFont
import random
import base64
from io import BytesIO

users = []

STATS = [
    "Hours spent sitting on the couch in the past week:",
    "Red Bulls consumed after 9 pm:",
    "Ankles broken (literal):",
    "HP:",
    "Zombies clipped:",
    "Time lost checking over your shoulder",
    "French zombies killed:",
    "New locations visited at night (dangerous):",
    "Caps gained in the last fiscal week:",
    "Number of new zombie followers:",
    "New LinkedIn connections made (non-zombie):",
]


@app.route("/")
def index():
    images = []

    for user in users:

        bg_im = Image.open("assets/template.png")
        bg_im = bg_im.resize((540, 960))

        random.seed(user.name)
        avatar = Image.open(f"assets/avatars/{random.randint(0, 7)}.jpeg")
        avatar = avatar.resize((275, 275))

        draw = ImageDraw.Draw(bg_im)
        font = ImageFont.truetype("assets/circular-std-medium-500.ttf", 40)
        small_font = ImageFont.truetype("assets/circular-std-medium-500.ttf", 20)

        bg_im.paste(avatar, (132, 120))

        draw.text((270, 550), user.name, (0, 0, 0), font=font, anchor="ms")

        random.seed()

        index = 0
        last_indices = []
        for i in range(3):
            while index in last_indices:
                index = random.randint(0, 10)
            last_indices.append(index)
            draw.text((20, 620 + i * 120), STATS[index], (0, 0, 0), font=small_font, anchor="ls")
            draw.text((20, 620 + i * 120 + 50), str(user.stats[index]), (0, 0, 0), font=font, anchor="ls")

        buffered = BytesIO()
        bg_im.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())

        images.append(img_str)

    random.seed()

    return render_template("index.html", users=users, images=images)


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")

    if request.method == "POST":
        choices = []

        if "username" not in request.form:
            return render_template("add_user.html", error="Name cannot be empty")

        for item in request.form.keys():
            if item != "username":
                choices.append(item)

        user = User(request.form.get("username"), choices)
        user.calculate_stats()
        users.append(user)

        return redirect(url_for("index"))
