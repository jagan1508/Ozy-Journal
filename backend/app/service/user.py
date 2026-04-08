from app.models.user import User
from sqlalchemy.orm import Session

async def create_user(db, user_data):
    existing = db.query(User).filter(User.email == user_data.email).first()
    if existing:
        return  None
    
    
    # hash password
    user = User(
        email=user_data.email,
        username=user_data.username,
        hashed_password=user_data.password  # temp
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if user.hashed_password != password:  # temp check
        return None
    return user

def get_all_users(db:Session):
    return db.query(User).all()