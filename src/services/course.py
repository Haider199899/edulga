from config import initialize_neo4j_connection
from fastapi import APIRouter, HTTPException, status
from schemas.course import CreateCourseRequest,AddModuleRequest,AddQuizRequest,PaginatedCourseQuery,CourseBase
from utils.helper import created_at, updated_at
from typing import Any
import uuid
cypher = initialize_neo4j_connection()

def create_course(course: CreateCourseRequest):
    # Generate a unique UUID for the course
    course_uuid = str(uuid.uuid4())
    
    # Prepare the query with parameters
    query = """
    CREATE (c:Course {id: $id, course_uuid: $course_uuid, title: $title, 
                      description: $description, department: $department, 
                      difficulty: $difficulty, prerequisites: $prerequisites, 
                      created_at: $created_at, updated_at: $updated_at})
    RETURN c
    """
    
    # Run the query with the parameters from the course object
    params = {
        "id": course.id,
        "course_uuid": course_uuid,
        "title": course.title,
        "description": course.description,
        "department": course.department,
        "difficulty": course.difficulty,
        "prerequisites": course.prerequisites,
        "created_at" : created_at,
        "updated_at" : updated_at
    }
    
    cypher.run(query, params)

    
    return params

def get_courses(getCourse: PaginatedCourseQuery) -> Any:
    query = f'MATCH (c:Course) RETURN c ORDER BY c.created_at {getCourse.sortOrder.value} SKIP {getCourse.offset} LIMIT {getCourse.limit}'
    print(query)
    results = cypher.run(query)
    records = []
    for result in results:
        records.append(result[0])
    return records

def create_module(course_uuid : str, module : AddModuleRequest):
    pass

def create_quiz(course_uuid : str,quiz : AddQuizRequest):
    pass