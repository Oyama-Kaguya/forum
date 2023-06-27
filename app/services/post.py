import datetime
import string
from typing import List, Dict
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql.operators import or_

from .user import UserORMHandler
from .utils import add_arguments
from app.models.post import Post, Comment


class PostORMHandler:
    def __init__(self, handler: scoped_session):
        self.handler = handler

    def add(self, args:List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        self.handler.add_all([Post.to_model(**item) for item in args])
        self.handler()

    def delete(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        for item in args:
            self.handler.query(Post).filter_by(post_id=item["post_id"]).delete()
        self.handler.commit()

    def update(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        pass

    def get_post(self, page: string):
        if self.handler is None:
            raise Exception("has no active db handler")
        return self.handler.query(Post).order_by(-Post.create_time).limit(30).offset(page * 30).all()


class CommentORMHandler:
    def __init__(self, handler: scoped_session):
        self.handler = handler

    def add(self, args:List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")

    def delete(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")

    # def update(self, args:List[Dict]):

