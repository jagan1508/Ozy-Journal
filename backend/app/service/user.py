from app.models.user import User

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