from sqlalchemy.orm import scoped_session

from .utils import BaseORMHandler
from app.models.banword import BanWord


class BanWordORMHandler(BaseORMHandler):
    def __init__(self, handler: scoped_session):
        super().__init__(BanWord, handler)
