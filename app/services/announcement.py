import datetime
from typing import List, Dict
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql.operators import or_

from .user import UserORMHandler
from .utils import add_arguments
from app.models.announcement import Announcement


class AnnouncementORMHandler:
    def __init__(self, handler: scoped_session):
        self.handler = handler

    @add_arguments(
        creaate_announcement=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    def add(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        self.handler.add_all([Announcement.to_model(**item) for item in args])
        self.handler.commit()

    def delete(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        for item in args:
            self.handler.query(Announcement).filter_by(announce_id=item["announce_id"]).delete()
        self.handler.commit()

    def get(self, user_id):
        user = UserORMHandler(self.handler).get(user_id)
        return self.handler.query(Announcement).filter(or_(Announcement.announce_type == "全局通知",
                                                           Announcement.announce_range == user.user_id)).all()

    def update(self, args: List[Dict]):
        pass
