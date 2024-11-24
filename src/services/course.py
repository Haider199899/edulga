from config import initialize_neo4j_connection
from fastapi import APIRouter, HTTPException, status,UploadFile
from schemas.course import CreateCourseRequest,AddModuleRequest,AddQuizRequest,PaginatedCourseQuery,CourseBase
from utils.helper import created_at, updated_at,extract_text_from_pdf, query_gpt,general_backbone
from utils.prompts import prompt_for_kg
from typing import Any
import uuid

# cypher = initialize_neo4j_connection()



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
    results = cypher.run(query)
    records = []
    for result in results:
        records.append(result[0])
    return records

def create_kg_from_pdf(file: UploadFile):
     # Extract text from PDF
    pdf_text = extract_text_from_pdf(file.file)
    if not pdf_text:
        raise HTTPException(status_code=400, detail="Failed to extract text from the PDF.")
    
    # Create a prompt for GPT-3.5 Turbo
    prompt = prompt_for_kg(pdf_text)
  
    # Query GPT-3.5 Turbo
    gpt_response = query_gpt(prompt)

    # Convert GPT response to JSON
    try:
        response_json = eval(gpt_response)  # Assuming GPT returns a valid Python dict
        return response_json
    except Exception as e:
        #create_kg_from_pdf(file)
        raise HTTPException(status_code=500, detail="Invalid JSON response from GPT-3.5.")



def create_quiz(course_uuid : str,quiz : AddQuizRequest):
    pass