from flask import Blueprint, request, jsonify

from app.extension import db
from app.services.message import MessageORMHandler

message_blueprint = Blueprint("message", __name__, url_prefix="/message")


@message_blueprint.route("/<int:user_id>", methods=["GET"])
def get(user_id: int):
    message_list = MessageORMHandler(db.session).get()
    return jsonify([
                       item.to_dict() for item in message_list
                   ] if message_list else {
        "msg_condition": "The user do not exist"
    })


@message_blueprint.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    if "message" not in data:
        return jsonify({
            "msg_condition": "格式错误"
        })
    data = data["message"]
    MessageORMHandler(db.session).add(data)
    return jsonify({
        "msg_condition": "success"
    })


@message_blueprint.route("/delete", methods=["POST"])
def delete():
    data = request.get_json()
    if "message" not in data:
        return jsonify({
            "msg_condition": "格式错误"
        })
    data = data["message"]
    MessageORMHandler(db.session).delete(data)
    return jsonify({
        "msg_condition": "success"
    })

