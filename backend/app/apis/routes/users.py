from fastapi import APIRouter, Depends,HTTPException
from app.schema.user import UserCreate,UserLogin,UserOut
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.service.user import create_user,get_all_users,authenticate_user

router=APIRouter()
@router.get("/")
async def read_root():
    return {"Message": "User API is working"}

@router.get("/all",response_model=list[UserOut])
async def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)
    

@router.post("/register")
async def register_user(user:UserCreate, db: Session = Depends(get_db)):
    new_user = await create_user(db, user)
    if not new_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return new_user


@router.post("/login",response_model=UserOut)
async def login(user: UserLogin,db: Session = Depends(get_db)):
    db_user=authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return db_user



