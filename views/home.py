from flask import Blueprint, render_template


homes = Blueprint('homes', __name__)


@homes.route("/home",)
def home():

    return render_template("home.html")