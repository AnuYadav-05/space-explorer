from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_db.db'

db.init_app(app)

# 🔐 Login manager setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Flask will redirect here if not logged in

# 🧠 User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app import routes