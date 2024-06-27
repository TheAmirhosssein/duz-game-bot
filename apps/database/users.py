from database.engine import Base, get_db
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, Sequence, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    username = Column(String(50), unique=True)

    def __repr__(self):
        return f"{self.username} = {self.name}"


async def get_user(username: str) -> User | None:
    db: Session = next(get_db())
    user = db.query(User).filter(User.username == username).first()
    return user


async def create_user(username: str, name: str) -> None:
    db: Session = next(get_db())
    new_user = User(name=name, username=username)
    db.add(new_user)
    db.commit()
