from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

flaskapp = Flask(__name__)
# this is flask app object
flaskapp.config.from_object(Config)
db=SQLAlchemy(flaskapp)
migrate=Migrate(flaskapp,db)

from app import routes, model