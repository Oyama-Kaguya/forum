from typing import List, Dict
from sqlalchemy.orm import scoped_session

from .user import UserORMHandler
from .utils import create_announcement
from app.models.announcement import Announcement


class AnnouncementORMHandler:
    def __init__(self, handler: scoped_session):
        self.handler = handler

    def add(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        announcement_list = []
        for item in [create_announcement(item) for item in args]:
            announcement = Announcement.to_model(**item)
            announcement_list.append(announcement)
        self.handler.add_all(announcement_list)
        self.handler.commit()

    def delete(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        for item in args:
            self.handler.query(Announcement).filter_by(announce_id=item["announce_id"]).delete()
        self.handler.commit()

    def update(self, args: List[Dict]):
        pass

    def get(self, user_id):
        user = UserORMHandler(self.handler).get(user_id)
        return self.handler.query(Announcement).filter_by(announce_type="全局通知")
