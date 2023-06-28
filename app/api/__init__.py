from .user import user_blueprint
from .announcement import announcement_blueprint
from .message import message_blueprint
from .post import post_blueprint
from .banword import ban_word_blueprint

DEFAULT_BLUEPRINT = [
    user_blueprint,
    announcement_blueprint,
    message_blueprint,
    post_blueprint,
    ban_word_blueprint
]


def config_blueprint(app):
    for blueprint in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint)
