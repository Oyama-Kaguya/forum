import datetime
from typing import List, Dict
from sqlalchemy.orm import scoped_session

from .utils import add_arguments, BaseORMHandler
from app.models.message import Message


class MessageORMHandler(BaseORMHandler):
    def __init__(self, handler: scoped_session):
        super().__init__(Message, handler)
