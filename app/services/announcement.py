import datetime
from typing import List, Dict
from flask_jwt_extended import current_user
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql.operators import or_

from .utils import add_arguments, BaseORMHandler
from app.models.announcement import Announcement


class AnnouncementORMHandler(BaseORMHandler):
    def __init__(self, handler: scoped_session):
        super().__init__(Announcement, handler)

    @add_arguments(
        announce_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    def add(self, args: Dict):
        print(args)
        super().add(args)

    def get(self):
        return self.handler.query(Announcement).filter(or_(Announcement.announce_type == "全局通知",
                                                           Announcement.announce_range == current_user)).all()

    def update(self, args: List[Dict]):
        pass
