from heroku import api
from heroku.routes.resources import Hello

import ujson

api.json_encoder = ujson.dumps

api.add_resource(Hello, "/api/hello")
