from typing import List, Dict
from sqlalchemy.orm import scoped_session


class BaseORMHandler:
    def __init__(self, cls, handler: scoped_session):
        self.cls = cls
        self.handler = handler

    def add(self, args: List[Dict]):
        if self.handler is None:
            raise Exception("has no active db handler")
        self.handler.add_all([self.cls.to_model(**item) for item in args])
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
        # user = UserORMHandler(self.handler).get(user_id)
        return self.handler.query(self.cls).filter_by(**kwargs).all()


def add_arguments(**kwargs):
    def out_wrapper(func):
        def wrapper(*args):
            for item in args:
                if isinstance(item, list):
                    for form in item:
                        for k, v in kwargs.items():
                            form[k] = v
            return func(*args)

        return wrapper

    return out_wrapper
