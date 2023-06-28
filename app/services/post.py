import datetime
from typing import List, Dict
from sqlalchemy.orm import scoped_session

from .utils import add_arguments, BaseORMHandler
from app.models.post import Post, Comment


class PostORMHandler(BaseORMHandler):
    def __init__(self, handler: scoped_session):
        super().__init__(Post, handler)

    @add_arguments(
        total_floor=1, floor=1,
        is_hidden=True, examine_state=1, is_topping=False,
        create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        modify_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    def add(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        for item in args:
            post = Post.to_model(**item)
            self.handler.add(post)
            self.handler.flush()
            post.comments = [Comment.to_model(**item, post_id=post.post_id)]
            self.handler.add(post)
        self.handler()

    def update(self):
        if self.handler is None:
            raise Exception("has no active db handler")
        pass

    def get_post_home(self):
        if self.handler is None:
            raise Exception("has no active db handler")
        # return self.handler.query(Post).order_by(-Post.create_time).limit(30).offset(page * 30).all()
        return self.handler.query(Post).order_by(-Post.create_time).all()

    def get_check(self):
        if self.handler is None:
            raise Exception("has no active db handler")
        return self.handler.query(Post).filter_by(examine_state=1).order_by(Post.create_time).all()\
            + self.handler.query(Comment).filter_by(examine_state=1).order_by(Comment.create_time).all()


class CommentORMHandler(BaseORMHandler):
    def __init__(self, handler: scoped_session):
        super().__init__(Comment, handler)

    @add_arguments(
        is_hidden=True, examine_state=1, is_topping=False,
        create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        modify_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    def add(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        post_list = []
        for item in args:
            post = Post.to_model(**item)

    def get(self, **kwargs):
        post = self.handler.query(Post).filter_by(post_id=kwargs["post_id"]).all()
        # commit_list = self.handler.query(Comment).filter_by(post_id=kwargs["post_id"])\
        #     .order_by(Comment.floor).limit(30).offset(kwargs["page"] * 30).all()
        commit_list = self.handler.query(Comment).filter_by(post_id=kwargs["post_id"])\
            .order_by(Comment.floor).all()
        return post, commit_list
