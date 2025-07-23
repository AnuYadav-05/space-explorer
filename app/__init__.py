from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # keep this safe

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from app import routes