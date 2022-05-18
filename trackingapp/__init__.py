# this file allows the execute file to recognize the market directory as a package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SECRET_KEY'] = 'd3c4fa20412642dd4c31c13d'
db = SQLAlchemy(app)

from trackingapp import routes
