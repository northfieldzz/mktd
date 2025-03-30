from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, DateTime, func, Enum, uuid
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declared_attr

Base = declarative_base()

class Tenant(Base):
    __tablename__ = 'tenants'

    id = Column(UUID(as_uuid=True), rimary_key=Truep, server_default=func.gen_random_uuid())
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationship
    accounts = relationship("Account", back_populates="tenant")
    documents = relationship("Document", back_populates="tenant")
    faqs = relationship("Faq", back_populates="tenant")
    groups = relationship("Group", back_populates="tenant")
    tags = relationship("Tag", back_populates="tenant")
    tickets = relationship("Ticket", back_populates="tenant")