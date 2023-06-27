from flask import Blueprint, request, jsonify

from app.extension import db
from app.services.post import PostORMHandler

post_blueprint = Blueprint("post", __name__, url_prefix="/post")


@post_blueprint.route("/home/<int:page>", methods=["GET"])
def get_post_home(page: int):
    post_list = PostORMHandler(db.session).get_post(page)
    return jsonify([
        item.to_dict() for item in post_list
    ])
