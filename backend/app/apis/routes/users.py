from fastapi import APIRouter, Depends,HTTPException
from app.schema.user import UserCreate,UserLogin
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.service.user import create_user

router=APIRouter()
@router.get("/")
async def read_root():
    return {"Message": "User API is working"}

@router.post("/register")
async def register_user(user:UserCreate, db: Session = Depends(get_db)):
    new_user = await create_user(db, user)
    if not new_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return new_user


@router.post("/login")
async def login(user: UserLogin):
    return {"message": "login logic here"}

