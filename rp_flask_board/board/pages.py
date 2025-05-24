from flask import Blueprint, render_template
#Pages program to connect all of the blueprints based on what is done in the reading

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/contact")
def contact():
    return render_template("pages/contact.html")
@bp.route("/projects")
def projects():
    return render_template("pages/projects.html")