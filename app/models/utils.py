from typing import Dict, Any
from sqlalchemy import DateTime, Numeric


def to_model(cls: Any, **kwargs) -> Any:
    cl = cls()
    columns = [c.name for c in cls.__table__.columns]
    for k, v in kwargs.items():
        if k in columns:
            setattr(cl, k, v)
    return cl


def to_dict(self: Any) -> Dict:
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def to_dict_specific(self: Any) -> Dict:
    res = {}
    for col in self.__table__.columns:
        if isinstance(col.type, DateTime):  # 判断类型是否为DateTime
            if not getattr(self, col.name):  # 判断实例中该字段是否有值
                value = ""
            else:  # 进行格式转换
                value = getattr(self, col.name).strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(col.type, Numeric):  # 判断类型是否为Numeric
            value = float(getattr(self, col.name))  # 进行格式转换
        else:  # 剩余的直接取值
            value = getattr(self, col.name)
        res[col.name] = value
    return res
