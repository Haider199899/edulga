from fastapi import APIRouter, HTTPException,status,Query,File, UploadFile, HTTPException
from src.schemas.course import CourseBase,CreateCourseRequest,PaginatedCourseQuery,GenerateRoadMapQuery
from src.services import course
from typing import Any,Annotated
import json
from fastapi.responses import JSONResponse
router = APIRouter()



@router.post("/courses", response_model=CourseBase, status_code=status.HTTP_201_CREATED)
async def create_course(addCourse: CreateCourseRequest):
    return course.create_course(addCourse)

@router.get("/get-courses", response_model=Any ,status_code=status.HTTP_200_OK)
def get_courses(getCourse: Annotated[PaginatedCourseQuery, Query()]) -> Any:
    return course.get_courses(getCourse)

@router.post("/create-kg-from-pdf", response_model=dict)
async def process_pdf(file: UploadFile = File(...)):
    """
    Endpoint to process a PDF file, extract text, and return a GPT-3.5 generated JSON response.
    """
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    return course.create_kg_from_pdf(file)

@router.get("/generate-roadmap")
def generate_roadmap_endpoint(roadmap: Annotated[GenerateRoadMapQuery, Query()]):
    """
    API endpoint to generate a learning roadmap.
    Expects a `query` string in the JSON body of the request.
    """
    data = roadmap
    query = data.query

    try:
        roadmap = course.generate_road_maps(query)
        return JSONResponse(content={"roadmap": roadmap}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    