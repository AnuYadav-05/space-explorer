from flask import render_template, redirect, url_for, request, flash, session
from app import app, db
from app.models import User
from app.forms import RegisterForm, LoginForm

from app.Gemini import GeminiClient
from app.NasaApod import NasaAPODClient
from app.NasaNeo import NasaNeoClient
from app.MarsRover import MarsRoverClient


@app.route("/")
def home():
    return render_template("home.html")


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

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            flash('Logged in!', 'success')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')