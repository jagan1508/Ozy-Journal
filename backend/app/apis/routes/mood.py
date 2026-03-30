from fastapi import APIRouter

router=APIRouter()
@router.get("/")
async def read_root():
    return {"Message": "Mood API is working"}

