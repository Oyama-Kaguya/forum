from flask import Blueprint, request, jsonify

from app.extension import db
from app.services.announcement import AnnouncementORMHandler

announcement_blueprint = Blueprint("announcement", __name__, url_prefix="/announcement")


@announcement_blueprint.route("/get/<int:user_id>", methods=["GET"])
def get(user_id: int):
    announcement_list = AnnouncementORMHandler(db.session).get(user_id)
    return jsonify([
        item.to_dict() for item in announcement_list
    ])


@announcement_blueprint.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    if "announcement" not in data:
        return jsonify({
            "msg_condition": "格式错误"
        })
    data = data["announcement"]
    AnnouncementORMHandler(db.session).add(data)
    return jsonify({
        "msg_condition": "success"
    })

@announcement_blueprint.route("/delete", methods=["POST"])
def delete():
    data = request.get_json()
    if "announcement" not in data:
        return jsonify({
            "msg_condition": "格式错误"
        })
    data = data["announcement"]
    AnnouncementORMHandler(db.session).delete(data)
    return jsonify({
        "msg_condition": "success"
    })
