# config.py

import pathlib
# import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
basedir = pathlib.Path(__file__).parent.resolve()
# connex_app = connexion.App(__name__, specification_dir=basedir)
connex_app= Flask(__name__)
app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'people.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)