from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.extension import db
from app.services.banword import BanWordORMHandler

ban_word_blueprint = Blueprint("ban_word", __name__, url_prefix="/ban_word")


@ban_word_blueprint.route("/add", methods=["POST"])
@jwt_required()
def add():
    BanWordORMHandler(db.session).add(request.get_json())
    return jsonify({
        "msg_condition": "success"
    })


@ban_word_blueprint.route("/<int:word_id>", methods=["DELETE"])
@jwt_required()
def delete(word_id: int):
    BanWordORMHandler(db.session).delete(message_id=word_id)
    return jsonify({
        "msg_condition": "success"
    })


@ban_word_blueprint.route("/", methods=["GET"])
@jwt_required()
def get():
    ban_word_list = BanWordORMHandler(db.session).get_all()
    return jsonify([item.to_dict() for item in ban_word_list])


@ban_word_blueprint.route("/delete", methods=["POST"])
@jwt_required()
def delete_args():
    data = request.get_json()
    if "message" not in data:
        return jsonify({
            "msg_condition": "格式错误"
        })
    BanWordORMHandler(db.session).delete_args(data["message"])
    return jsonify({
        "msg_condition": "success"
    })

