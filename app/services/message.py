import datetime
from typing import List, Dict
from sqlalchemy.orm import scoped_session

from .user import UserORMHandler
from .utils import add_arguments
from app.models.message import Message


class MessageORMHandler:
    def __init__(self, handler: scoped_session):
        self.handler = handler

    @add_arguments(
        create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    def add(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        self.handler.add_all([Message.to_model(**item) for item in args])
        self.handler.commit()

    def delete(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        for item in args:
            self.handler.query(Message).filter_by(message_id=item["message_id"]).delete()
        self.handler.commit()

    def get(self, user_id):
        user = UserORMHandler(self.handler).get(user_id)
        return self.handler.query(Message).filter_by()
