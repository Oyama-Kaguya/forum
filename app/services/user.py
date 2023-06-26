from typing import List, Dict, Optional
from sqlalchemy.orm import scoped_session

from .utils import create_user
from app.models.user import User, UserDetail, UserNickname, UserPortrait


class UserORMHandler:
    def __init__(self, handler: scoped_session):
        self.handler = handler

    def add(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        user_list = []
        for item in [create_user(item) for item in args]:
            user = User.to_model(**item)
            user.detail = UserDetail.to_model(**item)
            user.nickname = [UserNickname.to_model(**item)]
            user.portrait = [UserPortrait.to_model(**item)]
            user_list.append(user)
        self.handler.add_all(user_list)
        self.handler.commit()

    def delete(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        for item in args:
            self.handler.query(User).filter_by(user_id=item["user_id"]).delete()
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

    def get(self, user_id):
        return self.handler.query(User).filter_by(user_id=user_id).one_or_none()
