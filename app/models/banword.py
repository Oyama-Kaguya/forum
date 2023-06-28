from sqlalchemy import text

from app.extension import db
from .utils import to_model as tm, to_dict_specific as td


class BanWord(db.Model):
    __tablename__ = 'ban_word'

    word_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String(10), nullable=False, index=True)
    word = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, index=True, server_default=text("NOW()"))

    @classmethod
    def to_model(cls, **kwargs):
        return tm(cls, **kwargs)

    def to_dict(self):
        return td(self)
