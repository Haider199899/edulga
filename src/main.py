# main.py
from fastapi import FastAPI
from routers.course import router as courses_router


app = FastAPI()

# Include routers
app.include_router(courses_router, prefix="/api/courses", tags=["Courses"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
