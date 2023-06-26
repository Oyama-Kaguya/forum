from app.extension import db

from .utils import to_model as tm, to_dict_specific as td


# 母表 用户基本表
class Announcement(db.Model):  # 通知表
    __tablename__ = "announcement"

    announce_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String(10), nullable=False, index=True)
    announce_type = db.Column(db.Enum(
        "全局通知", "学院通知", "系通知", "专业通知", "个人通知"
    ), nullable=False)
    announce_range = db.Column(db.String(10), nullable=False)
    announce_content = db.Column(db.String(255), nullable=False)
    announce_time = db.Column(db.DateTime, nullable=False)

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)
