from .user import user_blueprint
from .announcement import announcement_blueprint

DEFAULT_BLUEPRINT = [
    user_blueprint,
    announcement_blueprint
]


def config_blueprint(app):
    for blueprint in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint)
