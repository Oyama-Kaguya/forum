import datetime
from typing import List, Dict
from sqlalchemy.orm import scoped_session

from flask_jwt_extended import current_user


def add_arguments(**kwargs):
    def out_wrapper(func):
        def wrapper(*args):
            print(args)
            for item in args:
                if isinstance(item, dict):
                    print(type(item))
                    for k, v in kwargs.items():
                        item[k] = v
            return func(*args)

        return wrapper

    return out_wrapper


class BaseORMHandler:
    def __init__(self, cls, handler: scoped_session):
        self.cls = cls
        self.handler = handler

    @add_arguments(
        create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        modify_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        user_id=current_user
    )
    def add(self, args: Dict):
        if self.handler is None:
            raise Exception("has no active db handler")
        self.handler.add(self.cls.to_model(**args))
        self.handler.commit()

    def delete(self, **kwargs):
        if self.handler is None:
            raise Exception("has no active db handler")
        self.handler.query(self.cls).filter_by(**kwargs).delete()
        self.handler.commit()

    def delete_args(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        for item in args:
            self.handler.query(self.cls).filter_by(**{k: v for k, v in item.items()
                                                      if k in [c.name for c in self.cls.__table__.columns]
                                                      }).delete()
        self.handler.commit()

    def get(self, **kwargs):
        if self.handler is None:
            raise Exception("has no active db handler")
        return self.handler.query(self.cls).filter_by(**kwargs).one_or_none()

    def get_all(self):
        if self.handler is None:
            raise Exception("has no active db handler")
        return self.handler.query(self.cls).filter_by().all()
