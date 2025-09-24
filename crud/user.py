
from sqlalchemy.orm import Session
from schemas.user import UserCreate

# create user
from db.models.all import User

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user