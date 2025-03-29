from sqlalchemy import Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Accounts(Base):
    __Tablename__ = 'accounts'

    id = Column(UUID, primary_key=True)
    