import datetime

from flask import Blueprint, request, jsonify
from app.extension import db
from app.services.user import UserORMHandler

user_blueprint = Blueprint('user', __name__, url_prefix="/user")


@user_blueprint.route('/get/<int:user_id>', methods=['GET'])
def get(user_id: int):
    return jsonify([item.to_dict() for item in
                    UserORMHandler(db.session()).get(user_id)])


@user_blueprint.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if "users" not in data:
        return "格式错误"
    data = data["users"]
    for item in data:
        item["create_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        item["last_login_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        item["nickname_text"] = "undefined"
        item["portrait_url"] = "undefined"
        item["birthday"] = "2000-1-1"
        item["gender"] = 1
        # item["grade"] = ""
        item["enrollment_date"] = "2000-1-1"
        item["graduation_date"] = "2000-1-1"
        item["major_id"] = "2000-1-1"
        item["is_show_birthday"] = False
        item["is_show_gender"] = False
        item["is_show_qq"] = False
        item["is_show_wechat"] = False
        item["is_email_show"] = False
        item["is_major_show"] = False
        item["is_name_show"] = False
        item["modify_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    UserORMHandler(db.session()).add(data)
    return "success"


@user_blueprint.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    if "users" not in data:
        return jsonify({
            "msg_condition": "Message Format Error"
        })
    data = data["users"]
    print("data", data)
    UserORMHandler(db.session()).delete(data)
    return jsonify({
        "msg_condition": "success"
    })


@user_blueprint.route('/update')
def update():
    data = request.get_json()
    print(data)
    if "users" not in data:
        return jsonify({
            "msg_condition": "格式错误"
        })
    data = data["users"]
    UserORMHandler(db.session()).update(data)
    return jsonify({
        "msg_condition": "success"
    })
