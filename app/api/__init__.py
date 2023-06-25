from .user import user

DEFAULT_BLUEPRINT = [
    (user, '/api/api')
]

def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)