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


@announcement_blueprint.route("/<int:user_id_or_announce_id>", methods=["GET", "DELETE"])
def get_and_delete(user_id_or_announce_id: int):
    if request.method == "GET":
        announcement_list = AnnouncementORMHandler(db.session).get(user_id_or_announce_id)
        return jsonify([
            item.to_dict() for item in announcement_list
        ])
    elif request.method == "DELETE":
        AnnouncementORMHandler(db.session).delete(announce_id=user_id_or_announce_id)
        return jsonify({
            "msg_condition": "success"
        })


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
