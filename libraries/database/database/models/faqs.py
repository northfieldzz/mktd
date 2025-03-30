from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, DateTime, func, Enum
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declared_attr

Base = declarative_base()

# FAQsテーブル
class FAQ(Base):
    __tablename__ = 'faqs'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    question = Column(String(255), nullable=False)
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
