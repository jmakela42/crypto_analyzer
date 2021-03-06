from flask import Flask
from config import config

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	from .api import api as api_blueprint
	app.register_blueprint(api_blueprint)

	from .helpers import helpers as helpers_blueprint
	app.register_blueprint(helpers_blueprint)

	return app