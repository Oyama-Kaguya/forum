from flask import Blueprint, request, jsonify

from app.extension import db
from app.services.announcement import AnnouncementORMHandler

announcement_blueprint = Blueprint("announcement", __name__, url_prefix="/announcement")


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


@announcement_blueprint.route("/announce_id>", methods=["DELETE"])
def delete(user_id_or_announce_id: int):
    AnnouncementORMHandler(db.session).delete(announce_id=user_id_or_announce_id)
    return jsonify({
        "msg_condition": "success"
    })


@announcement_blueprint.route("/", methods=["GET"])
def get():
    announcement_list = AnnouncementORMHandler(db.session).get(user_id=2020218023)
    return jsonify([
        item.to_dict() for item in announcement_list
    ])


@announcement_blueprint.route("/delete", methods=["POST"])
def delete_args():
    data = request.get_json()
    if "announcement" not in data:
        return jsonify({
            "msg_condition": "格式错误"
        })
    AnnouncementORMHandler(db.session).delete_args(data["announcement"])
    return jsonify({
        "msg_condition": "success"
    })
