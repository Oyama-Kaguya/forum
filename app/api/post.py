from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.extension import db
from app.services.post import PostORMHandler, CommentORMHandler

post_blueprint = Blueprint("post", __name__, url_prefix="/post")


@post_blueprint.route("/", methods=["POST"])
@jwt_required()
def add():
    PostORMHandler(db.session).add([request.get_json()])
    return jsonify({
        "msg_condition": "success"
    })


@post_blueprint.route("/<int:post_id>", methods=["DELETE"])
@jwt_required()
def delete_post(post_id: int):
    PostORMHandler(db.session).delete(post_id=post_id)
    return jsonify({
        "msg_condition": "success"
    })


@post_blueprint.route("/comment/<int:comment_id>", methods=["DELETE"])
@jwt_required()
def delete_comment(comment_id: int):
    CommentORMHandler(db.session).delete(comment_id=comment_id)
    return jsonify({
        "msg_condition": "success"
    })


@post_blueprint.route("/home", methods=["GET"])
@jwt_required()
def get_post_home():
    post_list = PostORMHandler(db.session).get_post_home()
    return jsonify([
        item.to_dict() for item in post_list
    ])


@post_blueprint.route("/<int:post_id>", methods=["GET"])
@jwt_required()
def get_post(post_id:int):
    args = request.args
    post, comment_list = CommentORMHandler(db.session).get(post_id=post_id)
    return jsonify(
        {
            "msg_condition": "success",
            "post": [item.to_dict() for item in post],
            "comment": [item.to_dict() for item in comment_list]
        } if post and comment_list else {
            "msg_condition": "The post do not exist"
        })


@post_blueprint.route("/check", methods=["GET"])
@jwt_required()
def get_check():
    check = [item.to_dict() for item in PostORMHandler(db.session).get_check()]
    for item in check:
        item["type"] = "title" \
            if "post_title" in item else "comment"
        item["content"] = item.pop("post_title") \
            if "post_title" in item else item.pop("comment_content")
    return jsonify(
        {
            "check": check
        }
    )
