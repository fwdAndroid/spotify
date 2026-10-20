from models.base import Base
from sqlalchemy import Column, TEXT, VARCHAR, LargeBinary


class User(Base):
    __tablename__ = 'users'

    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(1000))
    email = Column(VARCHAR(1000))
    password = Column(LargeBinary)
