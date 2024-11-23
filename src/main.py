# main.py
from fastapi import FastAPI
from routers.course import router as courses_router


app = FastAPI()

# Include routers
app.include_router(courses_router, prefix="/api/courses", tags=["Courses"])
# app.include_router(users_router, prefix="/api/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
