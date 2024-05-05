from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

flaskapp = Flask(__name__)
# this is flask app object
flaskapp.config.from_object(Config)
db=SQLAlchemy(flaskapp)
migrate=Migrate(flaskapp,db)
login = LoginManager(flaskapp)
login.login_view = 'login'

from app import routes, model