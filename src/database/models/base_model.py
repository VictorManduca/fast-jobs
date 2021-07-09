from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
  id: Any
  __name__: str

  @declared_attr
  def __tablename__(class_param)->str:
    return class_param.__name__.lower()