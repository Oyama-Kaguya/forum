import datetime
from typing import List, Dict
from sqlalchemy.orm import scoped_session

from .utils import add_arguments, BaseORMHandler
from app.models.user import User, UserDetail, UserNickname, UserPortrait


class UserORMHandler(BaseORMHandler):
    def __init__(self, handler: scoped_session):
        super().__init__(User, handler)

    def login(self, user_id, password):
        user = self.get_user(user_id=user_id)
        if user and user.check_password(password):
            return True
        return False

    @add_arguments(
        create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        modify_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        nickname_text="undefined", portrait_url="undefined", birthday="2000-1-1",
        gender=1, enrollment_date="2000-1-1", graduation_date="2000-1-1", major_id="23",
        is_show_birthday=False, is_show_gender=False, is_show_qq=False,
        is_show_wechat=False, is_email_show=False, is_major_show=False,
        is_name_show=False
    )
    def add(self, args: Dict):
        if self.handler is None:
            raise Exception("has no active db handler")
        user = User.to_model(**args)
        user.password(args["user_id"])
        user.detail = UserDetail.to_model(**args)
        user.nickname = [UserNickname.to_model(**args)]
        user.portrait = [UserPortrait.to_model(**args)]
        self.handler.add(user)
        self.handler.commit()

    def update(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        for item in args:
            if "user_id" not in item:
                continue
            user_id = item.pop("user_id")
            if "detail" in item:
                self.handler.query(UserDetail).filter_by(user_id=user_id).update(item.pop("detail"))
            self.handler.query(User).filter_by(user_id=user_id).update(item)
        self.handler.commit()

    def get_user(self, user_id):
        return self.handler.query(User).filter_by(user_id=user_id).one_or_none()

    def get_detail(self, user_id):
        return self.handler.query(UserDetail).filter_by(user_id=user_id).one_or_none()
