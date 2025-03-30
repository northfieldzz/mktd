from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, DateTime, func, Enum
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declared_attr

Base = declarative_base()

class TimeBaseModel(Base):
    