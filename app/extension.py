from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()


def config_extensions(app):
    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()