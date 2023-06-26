from sqlalchemy import text

from app.extension import db
from .utils import to_model as tm, to_dict_specific as td


# 母表 用户基本表
class User(db.Model):  # 账户表
    __tablename__ = "user_base"

    user_id = db.Column(db.String(10), primary_key=True)
    password_hash = db.Column(db.String(255, "utf8mb4_0900_ai_ci"), nullable=False)
    name = db.Column(db.String(10), nullable=False)
    card_number = db.Column(db.String(18), nullable=False)
    email = db.Column(db.String(50), nullable=False, index=True)
    user_group = db.Column(db.Integer, nullable=False)
    token = db.Column(db.String(64), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, server_default=text("NOW()"))
    last_login_time = db.Column(db.DateTime, nullable=False,
                                server_default=text("NOW()"), server_onupdate=text("NOW()"))

    detail = db.relationship("UserDetail", uselist=False, backref="user", cascade="all, delete")
    nickname = db.relationship("UserNickname", uselist=True, backref="user", cascade="all, delete")
    portrait = db.relationship("UserPortrait", uselist=True, backref="user", cascade="all, delete")

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)


# 子表 昵称表
class UserNickname(db.Model):
    __tablename__ = "user_nickname"

    nickname_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String(10), db.ForeignKey("user_base.user_id", ondelete="cascade"), nullable=False,
                        index=True)
    nickname_text = db.Column(db.String(20), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, server_default=text("NOW()"))

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)


# 子表 头像表
class UserPortrait(db.Model):
    __tablename__ = "usr_former_portrait"

    portrait_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String(10), db.ForeignKey("user_base.user_id", ondelete="cascade"), nullable=False,
                        index=True)
    portrait_url = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, server_default=text("NOW()"))

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)


# 子表 详细信息表
class UserDetail(db.Model):
    __tablename__ = "user_detail"

    user_id = db.Column(db.ForeignKey("user_base.user_id", ondelete="CASCADE"), primary_key=True)
    nickname_text = db.Column(db.String(20), nullable=False)
    portrait_url = db.Column(db.String(255), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    # grade = db.Column(db.Integer, nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False)
    graduation_date = db.Column(db.Date)
    qq_number = db.Column(db.String(11), info="QQ")
    wechat_number = db.Column(db.String(28), info="微信")
    email_show = db.Column(db.String(50), info="展示邮箱")
    major_id = db.Column(db.String(9), nullable=False, index=True)
    is_show_birthday = db.Column(db.Boolean, nullable=False, server_default=text("False"))
    is_show_gender = db.Column(db.Boolean, nullable=False, server_default=text("False"))
    is_show_qq = db.Column(db.Boolean, nullable=False, server_default=text("False"))
    is_show_wechat = db.Column(db.Boolean, nullable=False, server_default=text("False"))
    is_email_show = db.Column(db.Boolean, nullable=False, server_default=text("False"))
    is_major_show = db.Column(db.Boolean, nullable=False, server_default=text("False"))
    is_name_show = db.Column(db.Boolean, nullable=False, server_default=text("False"))
    modify_time = db.Column(db.DateTime, nullable=False, server_default=text("NOW()"), server_onupdate=text("NOW()"))

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)
