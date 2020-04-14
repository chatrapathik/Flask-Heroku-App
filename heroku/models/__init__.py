import json
from sys import exit as sys_exit

from elasticsearch import Elasticsearch

from heroku.configs import app_config

config_dict = app_config.configs

es_configs = config_dict.get("elasticsearch", {})
host = json.loads(es_configs.get("host", '["localhost"]'))
scheme = es_configs.get("scheme", "http")
port = es_configs.get("port", 9200)
username = es_configs.get("username")
password = es_configs.get("password")

auth_data = dict(scheme=scheme, port=port)

if username and password:
    auth_data["http_auth"] = (username, password)

try:
    ES = Elasticsearch(host, **auth_data)
except:
    app_config.logger.info("Something went bad while connecting to ES")
    sys_exit(1)
