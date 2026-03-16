from flask import Blueprint, render_template

second = Blueprint("second", __name__)

@second.route("/")
def home():
    return render_template("home.html")