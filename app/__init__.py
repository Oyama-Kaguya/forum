from flask import Flask
from app.api import config_blueprint
from app.extension import config_extensions

from config import configs


def create_app(config) -> Flask:
    app = Flask(__name__)

    app.config.from_object(configs[config])

    config_extensions(app)

    config_blueprint(app)

    return app
