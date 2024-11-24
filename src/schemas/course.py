from pydantic import BaseModel,Field
from typing import List, Optional
from constants.enums import SortOrder

# Define the request and response schemas
class CourseBase(BaseModel):
    id: str
    course_uuid: Optional[str] = None
    title: str
    description: str
    department: str
    difficulty: int
    prerequisites: Optional[str] = None  # Making prerequisites optional
    created_at: Optional[str] = None     # Making created_at optional
    updated_at: Optional[str] = None     # Making updated_at optional

class CreateCourseRequest(CourseBase):
    pass

class UpdateCourseRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    department: Optional[str] = None
    difficulty: Optional[int] = None
    prerequisites: Optional[List[str]] = None

class AddModuleRequest(BaseModel):
    course_uuid: str
    module_title: str
    module_description: Optional[str] = None

class AddQuizRequest(BaseModel):
    course_uuid: str
    quiz_title: str
    questions: List[dict]

class PaginatedCourseQuery(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)   # Default value is 10, ensuring limit is >= 1
    sortOrder: SortOrder = SortOrder.ASC

class GPTResponse(BaseModel):
    course: str
    topics: list