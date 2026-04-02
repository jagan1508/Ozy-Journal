from fastapi import FastAPI
from .apis.routes import users,mood,suggestions
from app.db.init_db import init_db

app = FastAPI(title="Mood Journal",version="1.0.0")

#Routes
app.include_router(users.router,prefix="/users",tags=["Users"])
app.include_router(mood.router,prefix="/mood",tags=["Mood"])
app.include_router(suggestions.router,prefix="/suggestions",tags=["Suggestions"])


@app.on_event("startup")
def startup():
    init_db()



@app.get("/")
def read_root():
    return {"Message": "API is working"}

@app.on_event("startup")
async def startup_event():
    print("🚀 Server started")
    
@app.on_event("shutdown")
async def startup_event():
    print("Server stopped !!")

