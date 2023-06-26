from sqlalchemy import text

from app.extension import db
from .utils import to_model as tm, to_dict_specific as td


class Message(db.Model):  # 留言表
    __tablename__ = 'messages'

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String(10), nullable=False, index=True)
    message_content = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, index=True, server_default=text("NOW()"))

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)
#
# class NcNotification(db.Model):  # 通知表
#     __tablename__ = 'nc_notifications'
#
#     nc_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.ForeignKey('usr_base.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False,
#                         index=True)
#     nc_type = db.Column(db.Integer, nullable=False)
#     nc_range = db.Column(db.String(10), nullable=False, info='通知范围')
#     nc_content = db.Column(db.String(255), nullable=False)
#     nc_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
#
#     user = db.relationship('UsrBase', primaryjoin='NcNotification.user_id == UsrBase.user_id',
#                            backref='nc_notifications')
#
#
# class PsComment(db.Model):  # 评论表
#     __tablename__ = 'ps_comments'
#
#     comment_id = db.Column(db.Integer, primary_key=True)
#     ps_id = db.Column(db.ForeignKey('ps_posts.ps_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False,
#                       index=True)
#     user_id = db.Column(db.ForeignKey('usr_base.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False,
#                         index=True)
#     comment_content = db.Column(db.String(255), nullable=False)
#     floor = db.Column(db.Integer, nullable=False)
#     create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
#     modify_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
#
#     ps = db.relationship('PsPost', primaryjoin='PsComment.ps_id == PsPost.ps_id', backref='ps_comments')
#     user = db.relationship('UsrBase', primaryjoin='PsComment.user_id == UsrBase.user_id', backref='ps_comments')
#
#
# class PsPost(db.Model):  # 帖子表
#     __tablename__ = 'ps_posts'
#
#     ps_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.ForeignKey('usr_base.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False,
#                         index=True)
#     ps_type = db.Column(db.Integer, nullable=False)
#     ps_title = db.Column(db.String(50), nullable=False)
#     create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
#     is_hidden = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='（0：不隐藏，1：隐藏）')
#     is_examine = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(),
#                            info='（0：审核通过，1：审核中，-1：审核不通过）')
#     is_topping = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='（0：不置顶）')
#
#     user = db.relationship('UsrBase', primaryjoin='PsPost.user_id == UsrBase.user_id', backref='ps_posts')
