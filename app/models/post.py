from sqlalchemy import text

from app.extension import db
from .utils import to_model as tm, to_dict_specific as td


# 母表 帖子表
class Post(db.Model):
    __tablename__ = 'post'

    post_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String(10), nullable=False, index=True)
    post_type = db.Column(db.Integer, nullable=False)
    post_title = db.Column(db.String(50), nullable=False)
    total_floor = db.Column(db.Integer, nullable=False)
    is_hidden = db.Column(db.Boolean, nullable=False, server_default=text("True"))
    #  0：审核通过、1：审核中、2：审核不通过
    is_examine = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    is_topping = db.Column(db.Boolean, nullable=False, server_default=text("False"))
    create_time = db.Column(db.DateTime, nullable=False, index=True, server_default=text("NOW()"))

    comments = db.relationship("Comment", uselist=True, backref="post", cascade="all, delete")

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)


# 子表 评论表
class Comment(db.Model):  # 评论表
    __tablename__ = 'comment'

    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    post_id = db.Column(db.ForeignKey('post.post_id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.String(10), nullable=False, index=True)
    comment_content = db.Column(db.String(255), nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    is_hidden = db.Column(db.Boolean, nullable=False, server_default=text("True"))
    #  0：审核通过、1：审核中、2：审核不通过
    examine_state = db.Column(db.Integer, nullable=False, server_default=text("1"))
    is_topping = db.Column(db.Boolean, nullable=False, server_default=text("False"))
    create_time = db.Column(db.DateTime, nullable=False, server_default=text("NOW()"))
    modify_time = db.Column(db.DateTime, nullable=False,
                            server_default=text("NOW()"), server_onupdate=text("NOW()"))

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)
