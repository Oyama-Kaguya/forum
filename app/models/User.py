import datetime

from ..extension import db


class UsrBase(db.Model):  # 账户表
    __tablename__ = 'usr_base'

    user_id = db.Column(db.String(10), primary_key=True)
    password_hash = db.Column(db.String(255, 'utf8mb4_0900_ai_ci'), nullable=False)
    email = db.Column(db.String(50), nullable=False, index=True)
    user_group = db.Column(db.Integer, nullable=False)
    token = db.Column(db.String(64), nullable=False)
    last_login_time = db.Column(db.DateTime, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
