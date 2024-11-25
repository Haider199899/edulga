from src.config import initialize_neo4j_connection
from fastapi import APIRouter, HTTPException, status,UploadFile
from src.schemas.course import CreateCourseRequest,AddModuleRequest,AddQuizRequest,PaginatedCourseQuery,CourseBase
from src.utils.helper import created_at, updated_at,extract_text_from_pdf, query_gpt,general_backbone
from src.utils.prompts import prompt_for_kg
from typing import Any
from dotenv import load_dotenv
import uuid
import json
import os
from langchain_openai import ChatOpenAI
load_dotenv()
# API Key for OpenAI
api_key = os.getenv("OPENAI_API_KEY")
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
    gpt_response = query_gpt(prompt,"gpt-3.5-turbo")

    # Convert GPT response to JSON
    try:
        response_json = json.loads(gpt_response)  # Assuming GPT returns a valid Python dict
        return response_json
    except Exception as e:
        #create_kg_from_pdf(file)
        raise HTTPException(status_code=500, detail="Invalid JSON response from GPT-3.5.")
    
def generate_road_maps(query: str) -> dict:
    """
    Generates a roadmap based on the query using OpenAI.
    Returns the roadmap as a Python dictionary.
    """
    # Initialize the ChatOpenAI model
    #llm = ChatOpenAI(model="gpt-4", api_key=api_key)

    # Updated Prompt
    # Updated Prompt
    prompt = f"""
    You are an expert in creating structured, step-by-step learning roadmaps to help individuals achieve mastery in specific topics.
    Generate a JSON representation of a **directed learning roadmap** based on the user's query. Ensure the relationships clearly show the order of learning.

    The output should include:
    - `entity1`: The main concept or higher-level topic.
    - `entity2`: The subtopic or concept that depends on `entity1`.
    - `relationship`: Describe the connection (e.g., "prerequisite for", "includes", "builds upon").
    - `priority`: A number indicating the order in which the concepts should be learned, where lower numbers are learned first. No two nodes should have the same priority, and the graph should reflect a clear progression.

    ### Query:
    {query}
    """

    # Generate response from OpenAI
    try:
        response = query_gpt(prompt,"gpt-4o")
    except Exception as e:
        raise Exception(f"Error interacting with OpenAI: {str(e)}")

    # Parse and clean the JSON response
    try:
        # # Clean the response to remove markdown and ensure valid JSON
        # cleaned_response = response.strip('```json').strip('```').strip()

        # # Ensure the response is not empty
        # if not cleaned_response:
        #     raise ValueError("Received empty response after cleaning.")

        # Parse the cleaned JSON response
        cleaned_response = response.strip('```json').strip('```').strip()
        roadmap = json.loads(cleaned_response)

    except json.JSONDecodeError as e:
        raise Exception(f"Error parsing OpenAI response: {str(e)}, response: {response}")
    except ValueError as e:
        raise Exception(f"Received empty or invalid response: {str(e)}")

    return roadmap



def create_quiz(course_uuid : str,quiz : AddQuizRequest):
    pass