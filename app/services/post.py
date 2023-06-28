import datetime
from typing import Dict
from sqlalchemy.orm import scoped_session
from flask_jwt_extended import current_user
from sqlalchemy.sql.operators import and_

from .utils import add_arguments, BaseORMHandler
from app.models.post import Post, Comment, Check


class PostORMHandler(BaseORMHandler):
    def __init__(self, handler: scoped_session):
        super().__init__(Post, handler)

    @add_arguments(
        total_floor=1, floor=1, user_id=current_user,
        is_hidden=True, examine_state=1, is_topping=False
    )
    def add(self, args: Dict):
        if self.handler is None:
            raise Exception("has no active db handler")
        post = Post.to_model(**args)
        self.handler.add(post)
        self.handler.flush()
        post.comments = [Comment.to_model(**args, post_id=post.post_id)]
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
        return self.handler.query(Post).filter_by(is_hidden=False).order_by(-Post.create_time).all()

    def get_check(self):
        if self.handler is None:
            raise Exception("has no active db handler")
        return self.handler.query(Post).filter_by(examine_state=1).order_by(Post.create_time).all() \
            + self.handler.query(Comment).filter_by(examine_state=1).order_by(Comment.create_time).all()

    @add_arguments(
        user_id=current_user,
        create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    def check(self, checked_id, passing: bool):
        if self.handler is None:
            raise Exception("has no active db handler")
        #  审核通过
        if passing:
            self.handler.query(Post).filter_by(post_id=checked_id).update({"examine_state": 0, "is_hidden": False})
            self.handler.commit()
        #  审核不通过
        else:
            self.handler.query(Post).filter_by(post_id=checked_id).update({"examine_state": 2, "is_hidden": True})
            self.handler.commit()


class CommentORMHandler(BaseORMHandler):
    def __init__(self, handler: scoped_session):
        super().__init__(Comment, handler)

    @add_arguments(
        is_hidden=True, examine_state=1, is_topping=False,
        create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        modify_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    def add(self, args: Dict):
        super().add(args)

    def get(self, **kwargs):
        post = self.handler.query(Post).filter_by(post_id=kwargs["post_id"]).all()
        # commit_list = self.handler.query(Comment).filter_by(post_id=kwargs["post_id"])\
        #     .order_by(Comment.floor).limit(30).offset(kwargs["page"] * 30).all()
        commit_list = self.handler.query(Comment).filter(and_(Comment.post_id == kwargs["post_id"],
                                                              Comment.is_hidden == False)).order_by(Comment.floor).all()
        return post, commit_list


class CheckORMHandler(BaseORMHandler):
    def __init__(self, handler: scoped_session):
        super().__init__(Check, handler)
