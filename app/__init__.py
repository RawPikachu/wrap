import os
from flask import Flask

app = Flask("Wrap", static_folder="assets", static_url_path="/assets")

from app import views
