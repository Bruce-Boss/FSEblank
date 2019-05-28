from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='static')
app.config.from_object('config')
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from . import views, models
