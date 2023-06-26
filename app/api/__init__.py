from .user import user_blueprint

DEFAULT_BLUEPRINT = [
    user_blueprint
]


def config_blueprint(app):
    for blueprint in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint)
