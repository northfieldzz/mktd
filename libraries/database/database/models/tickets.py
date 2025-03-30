from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, DateTime, func, Enum, UUID
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declared_attr

Base = declarative_base()

# Ticketsテーブル
class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    tenant_id = Column(UUID(as_uuid=True), nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.id', ondelete='CASCADE'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String(50), nullable=False, default='open')
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationship
    tenant_id = relationship("Tenant", back_populates="tenants")
    account = relationship("Account", back_populates="tickets")
