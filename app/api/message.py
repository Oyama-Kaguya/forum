from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.extension import db
from app.services.message import MessageORMHandler

message_blueprint = Blueprint("message", __name__, url_prefix="/message")


@message_blueprint.route("/add", methods=["POST"])
@jwt_required()
def add():
    MessageORMHandler(db.session).add([request.get_json()])
    return jsonify({
        "msg_condition": "success"
    })


@message_blueprint.route("/<int:message_id>", methods=["DELETE"])
@jwt_required()
def delete(message_id: int):
    MessageORMHandler(db.session).delete(message_id=message_id)
    return jsonify({
        "msg_condition": "success"
    })


@message_blueprint.route("/", methods=["GET"])
@jwt_required()
def get():
    message_list = MessageORMHandler(db.session).get_all()
    return jsonify([
                       item.to_dict() for item in message_list
                   ] if message_list else {
        "msg_condition": "The user do not exist"
    })


@message_blueprint.route("/delete", methods=["POST"])
@jwt_required()
def delete_args():
    data = request.get_json()
    if "message" not in data:
        return jsonify({
            "msg_condition": "格式错误"
        })
    MessageORMHandler(db.session).delete_args(data["message"])
    return jsonify({
        "msg_condition": "success"
    })

