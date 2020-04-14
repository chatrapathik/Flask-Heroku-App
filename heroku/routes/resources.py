import json

from flask import request, render_template, make_response, session, redirect, g
from flask_restful import Resource

from heroku.models import ES
from heroku.configs import app_config

class Hello(Resource):
    """

    """
    def get(self):
        return "Hello world"