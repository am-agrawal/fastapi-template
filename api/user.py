from fastapi import APIRouter, Depends, HTTPException
from schemas.user import UserCreate, UserRead
import crud.user as user_crud
from db.session import get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/", response_model=UserRead)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.create_user(db, user)
    return db_user
