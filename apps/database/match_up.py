import datetime
from enum import Enum

from database.engine import Base, get_db
from database.users import User
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Sequence, String
from sqlalchemy.orm import Session, relationship


class StatusEnum(Enum):
    started = "ST"
    failed = "FA"
    accepted = "AC"


class MatchUp(Base):
    __tablename__ = "match_ups"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    responder_id = Column(Integer, ForeignKey(User.id), nullable=True)
    status = Column(String(3), nullable=False)
    created_at = Column(DateTime(), default=datetime.datetime.now())

    user = relationship("User", foreign_keys="MatchUp.user_id")
    responder = relationship("User", foreign_keys="MatchUp.responder_id")


async def has_open_request(user: User) -> bool:
    db: Session = next(get_db())
    match_up = (
        db.query(MatchUp)
        .filter(
            MatchUp.user == user,
            MatchUp.status == StatusEnum.started.value,
        )
        .first()
    )
    return match_up is not None


async def matched_with_someone(user: User) -> bool:
    db: Session = next(get_db())
    match_up = (
        db.query(MatchUp)
        .filter(
            MatchUp.responder == user,
            MatchUp.status == StatusEnum.accepted.value,
        )
        .first()
    )
    return match_up is not None


async def create_match_up(user: User):
    db: Session = next(get_db())
    new_match_up = MatchUp(user_id=user.id, status=StatusEnum.started.value)
    db.add(new_match_up)
    db.commit()


async def open_request(user: User) -> bool:
    db: Session = next(get_db())
    open_match_ups = db.query(MatchUp).filter(
        MatchUp.status == StatusEnum.started.value, MatchUp.user_id != user.id
    )
    return open_match_ups.count() != 0


async def match_with_player(user: User) -> User:
    db: Session = next(get_db())
    user = db.merge(user)
    open_match_up = (
        db.query(MatchUp)
        .filter(
            MatchUp.status == StatusEnum.started.value,
            MatchUp.user_id != user.id,
        )
        .first()
    )
    assert open_match_up is not None
    open_match_up.responder = user
    db.commit()
    return open_match_up.user
