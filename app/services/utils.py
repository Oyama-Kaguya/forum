from typing import List, Dict
from sqlalchemy.orm import scoped_session

from app.extension import db


class BaceORMHandler:
    def __init__(self, cls, handler: scoped_session):
        self.cls = cls
        self.handler = handler

    def add(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        self.handler.add_all([self.cls.to_model(**item) for item in args])
        self.handler.commit()

    def delete(self, args: List[Dict], **kwargs):
        if self.handler is None:
            raise Exception("has no active db handler")
        for item in args:
            for k, v in kwargs.items():
                kwargs[k] = item[v]
                self.handler.query(self.cls).filter_by(**kwargs).delete()
        self.handler.commit()

    def get(self, **kwargs):
        if self.handler is None:
            raise Exception("has no active db handler")
        # user = UserORMHandler(self.handler).get(user_id)
        return self.handler.query(self.cls).filter_by(**kwargs).all()

def add_arguments(**kwargs):
    def out_wrapper(func):
        def wrapper(*args):
            for item in args:
                if isinstance(item, list):
                    for form in item:
                        for k, v in kwargs.items():
                            form[k] = v
            return func(*args)

        return wrapper

    return out_wrapper

# def create_announcement(announce: dict) -> dict:
#     announce["announce_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     return announce

# 为新用户创建初始信息
# def create_user(user: dict) -> dict:
#     pass  # 输入合法性校验
#     user["create_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     user["last_login_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     user["nickname_text"] = "undefined"
#     user["portrait_url"] = "undefined"
#     user["birthday"] = "2000-1-1"
#     user["gender"] = 1
#     # user["grade"] = ""
#     user["enrollment_date"] = "2000-1-1"
#     user["graduation_date"] = "2000-1-1"
#     user["major_id"] = "2000-1-1"
#     user["is_show_birthday"] = False
#     user["is_show_gender"] = False
#     user["is_show_qq"] = False
#     user["is_show_wechat"] = False
#     user["is_email_show"] = False
#     user["is_major_show"] = False
#     user["is_name_show"] = False
#     user["modify_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     return user
