from fastapi import APIRouter, HTTPException,status,Query
from schemas.course import CourseBase,CreateCourseRequest,PaginatedCourseQuery
from services import course
from typing import Any,Annotated
router = APIRouter()

@router.post("/courses", response_model=CourseBase, status_code=status.HTTP_201_CREATED)
async def create_course(addCourse: CreateCourseRequest):
    return course.create_course(addCourse)

@router.get("/get-courses", response_model=Any ,status_code=status.HTTP_200_OK)
def get_courses(getCourse: Annotated[PaginatedCourseQuery, Query()]) -> Any:
    return course.get_courses(getCourse)

# @router.put("/courses/{course_id}", response_model=CourseBase)
# def update_course(course_id: str, updates: UpdateCourseRequest):
#     return update_course_service(course_id, updates)

# @router.post("/courses/{course_id}/modules", response_model=AddModuleRequest)
# def add_module(course_id: str, module: AddModuleRequest):
#     return add_module_service(course_id, module)

# @router.post("/courses/{course_id}/quizzes", response_model=AddQuizRequest)
# def add_quiz(course_id: str, quiz: AddQuizRequest):
#     return add_quiz_service(course_id, quiz)

