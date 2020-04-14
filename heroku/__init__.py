import os

from flask import Flask, jsonify
from flask_restful import Api

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# app
app = Flask(__name__, static_folder=APP_ROOT + "/static")
api = Api(app)


# Routes
import heroku.routes.routes

from .app_runner import runner
from heroku.models import ES
from heroku.configs import app_config
