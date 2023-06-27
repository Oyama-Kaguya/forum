from flask import Blueprint, request, jsonify

from app.extension import db
from app.services.post import PostORMHandler, CommentORMHandler

post_blueprint = Blueprint("post", __name__, url_prefix="/post")


@post_blueprint.route("/home", methods=["GET"])
def get_post_home(page: int):
    post_list = PostORMHandler(db.session).get_post_home()
    return jsonify([
        item.to_dict() for item in post_list
    ])


@post_blueprint.route("/", methods=["GET"])
def get_post():
    post_id = request.args.get("post_id")
    page = request.args.get("page")
    post, comment_list = CommentORMHandler(db.session).get(post_id=post_id, page=page)
    return jsonify(
        {
            "msg_condition": "success",
            "post": [item.to_dict() for item in post],
            "comment": [item.to_dict() for item in comment_list]
        } if post and comment_list else {
            "msg_condition": "The post do not exist"
        })
