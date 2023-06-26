from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()


def config_extensions(app):
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    with app.app_context():
        db.create_all()