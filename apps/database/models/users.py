from database.engine import Base
from sqlalchemy import Column, Integer, Sequence, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    username = Column(String(50))

    def __repr__(self):
        return f"{self.username} = {self.name}"
