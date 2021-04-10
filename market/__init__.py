from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'd755b70a6f4644df18312f57'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from market import routes