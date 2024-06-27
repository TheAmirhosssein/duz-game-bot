from database.engine import Base
from database.users import User
from sqlalchemy import Column, ForeignKey, Integer, Sequence, String, DateTime
from sqlalchemy.orm import relationship
import datetime


class MatchUp(Base):
    __tablename__ = "match_ups"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    responder_id = Column(Integer, ForeignKey(User.id), primary_key=True, nullable=True)
    status = Column(String(3))
    created_at = Column(DateTime(), default=datetime.datetime.now())

    user = relationship("User", foreign_keys="MatchUp.user_id")
    responder = relationship("User", foreign_keys="MatchUp.responder_id")
