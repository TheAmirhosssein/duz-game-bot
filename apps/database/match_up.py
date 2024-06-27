import datetime
from enum import Enum

from database.engine import Base, get_db
from database.users import User
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Sequence, String
from sqlalchemy.orm import Session, relationship


class StatusEnum(Enum):
    started: str = "ST"
    failed: str = "FA"
    accepted: str = "AC"


class MatchUp(Base):
    __tablename__ = "match_ups"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    responder_id = Column(Integer, ForeignKey(User.id), nullable=True)
    status = Column(String(3), nullable=False)
    created_at = Column(DateTime(), default=datetime.datetime.now())

    user = relationship("User", foreign_keys="MatchUp.user_id")
    responder = relationship("User", foreign_keys="MatchUp.responder_id")


async def can_request(user: User):
    db: Session = next(get_db())
    match_up = (
        db.query(MatchUp)
        .filter(MatchUp.user_id == user.id, MatchUp.status == StatusEnum.started.value)
        .first()
    )
    return match_up is None


async def create_match_up(user: User):
    db: Session = next(get_db())
    new_match_up = MatchUp(user_id=user.id, status=StatusEnum.started.value)
    db.add(new_match_up)
    db.commit()
