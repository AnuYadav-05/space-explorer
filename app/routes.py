from app import app
from flask import render_template, request

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/docs")
def docs():
    return render_template("docs.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
