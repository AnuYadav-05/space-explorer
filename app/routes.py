from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app

from app import db
from app.models import User
from app.forms import RegisterForm, LoginForm
from app.forms import ContactForm 

from app.Gemini import GeminiClient
from app.NasaApod import NasaAPODClient
from app.NasaNeo import NasaNeoClient
from app.MarsRover import MarsRoverClient


@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route("/api/links")
def api_links():
    return render_template("api_links.html")


@app.route("/api/gem", methods=["GET", "POST"])
def api_gem():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")
        if question:
            gemini = GeminiClient()
            try:
                answer = gemini.ask(question)
            except Exception as e:
                answer = f"Error: {e}"
    return render_template("gemini_test.html", answer=answer)


@app.route("/api/nasa/apod", methods=["GET", "POST"])
def api_nasa_apod():
    apod_data = None
    if request.method == "POST":
        date = request.form.get("date")
        apod_client = NasaAPODClient()
        apod_data = apod_client.get_apod(date)
    return render_template("apod_test.html", apod=apod_data)


@app.route("/api/nasa/neo", methods=["GET", "POST"])
def api_nasa_neo():
    neo_data = None
    if request.method == "POST":
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        neo_client = NasaNeoClient()
        neo_data = neo_client.get_neo_feed(start_date, end_date)
    return render_template("neo_test.html", neo=neo_data)


@app.route("/api/nasa/rover", methods=["GET", "POST"])
def api_nasa_rover():
    rover_data = None
    if request.method == "POST":
        rover = request.form.get("rover", "curiosity")
        sol = request.form.get("sol", 1000)
        camera = request.form.get("camera")
        rover_client = MarsRoverClient()
        rover_data = rover_client.get_photos(rover, sol, camera)
    return render_template("rover_test.html", rover=rover_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/docs")
def docs():
    return render_template("docs.html")


@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")



@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("Message sent successfully!", "success")
        return redirect(url_for("dashboard"))
    return render_template("contact.html", form=form)

@app.route("/system-check")
def system_check():
    return "System Check Passed!"

@app.route("/logs")
def logs():
    return "logs"

@app.route("/new_mission")
def new_mission():
    return "new_mission"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Logged in!", "success")
            return redirect(url_for("dashboard"))
        flash("Invalid credentials", "danger")
    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.route("/reset_password_request")
def reset_password_request():
    return "Password reset page coming soon."


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
