import datetime
from typing import List, Dict
from sqlalchemy.orm import scoped_session

from .utils import add_arguments, BaseORMHandler
from app.models.message import Message


class MessageORMHandler(BaseORMHandler):
    def __init__(self, handler: scoped_session):
        super().__init__(Message, handler)

    @add_arguments(
        create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    def add(self, args: List[Dict]):
        super().add(args)

    def delete(self, args: List[Dict], **kwargs):
        super().delete(args, message_id="message_id")
