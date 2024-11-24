from datetime import datetime
from fastapi import HTTPException, HTTPException
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv
load_dotenv()
import openai
import openai
from dotenv import load_dotenv
load_dotenv()
# Set your OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
# Get current timestamp
current_timestamp = datetime.now()
created_at = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
updated_at = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
deleted_at = None

def extract_text_from_pdf(pdf_file):
    """
    Extract text from an uploaded PDF file.
    """
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting text: {str(e)}")

def query_gpt(prompt: str):
    """
    Query GPT-3.5 Turbo with a given prompt.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error querying GPT-3.5 Turbo: {str(e)}")
    
def general_backbone() -> str:
    return """
    [
    {"entity1": "Mathematics", "entity2": "Algebra", "relationship": "has subtopic"},
    {"entity1": "Mathematics", "entity2": "Calculus", "relationship": "has subtopic"},
    {"entity1": "Mathematics", "entity2": "Geometry", "relationship": "has subtopic"},
    {"entity1": "Mathematics", "entity2": "Statistics", "relationship": "has subtopic"},
    {"entity1": "Mathematics", "entity2": "Number Theory", "relationship": "has subtopic"},
    {"entity1": "Mathematics", "entity2": "Topology", "relationship": "has subtopic"},
    {"entity1": "Mathematics", "entity2": "Combinatorics", "relationship": "has subtopic"},
    {"entity1": "Mathematics", "entity2": "Discrete Mathematics", "relationship": "has subtopic"},
    {"entity1": "Mathematics", "entity2": "Mathematical Logic", "relationship": "has subtopic"},
    {"entity1": "Mathematics", "entity2": "Applied Mathematics", "relationship": "has subtopic"},
    {"entity1": "Computer Science", "entity2": "Algorithms", "relationship": "has subtopic"},
    {"entity1": "Computer Science", "entity2": "Data Structures", "relationship": "has subtopic"},
    {"entity1": "Computer Science", "entity2": "Artificial Intelligence", "relationship": "has subtopic"},
    {"entity1": "Computer Science", "entity2": "Machine Learning", "relationship": "has subtopic"},
    {"entity1": "Computer Science", "entity2": "Software Engineering", "relationship": "has subtopic"},
    {"entity1": "Computer Science", "entity2": "Web Development", "relationship": "has subtopic"},
    {"entity1": "Computer Science", "entity2": "Cybersecurity", "relationship": "has subtopic"},
    {"entity1": "Computer Science", "entity2": "Database Systems", "relationship": "has subtopic"},
    {"entity1": "Computer Science", "entity2": "Human-Computer Interaction", "relationship": "has subtopic"},
    {"entity1": "Computer Science", "entity2": "Computer Networks", "relationship": "has subtopic"},
    {"entity1": "Physics", "entity2": "Classical Mechanics", "relationship": "has subtopic"},
    {"entity1": "Physics", "entity2": "Quantum Mechanics", "relationship": "has subtopic"},
    {"entity1": "Physics", "entity2": "Thermodynamics", "relationship": "has subtopic"},
    {"entity1": "Physics", "entity2": "Electromagnetism", "relationship": "has subtopic"},
    {"entity1": "Physics", "entity2": "Relativity", "relationship": "has subtopic"},
    {"entity1": "Physics", "entity2": "Astrophysics", "relationship": "has subtopic"},
    {"entity1": "Physics", "entity2": "Nuclear Physics", "relationship": "has subtopic"},
    {"entity1": "Physics", "entity2": "Particle Physics", "relationship": "has subtopic"},
    {"entity1": "Physics", "entity2": "Condensed Matter Physics", "relationship": "has subtopic"},
    {"entity1": "Physics", "entity2": "Optics", "relationship": "has subtopic"},
    {"entity1": "Biology", "entity2": "Cell Biology", "relationship": "has subtopic"},
    {"entity1": "Biology", "entity2": "Genetics", "relationship": "has subtopic"},
    {"entity1": "Biology", "entity2": "Evolutionary Biology", "relationship": "has subtopic"},
    {"entity1": "Biology", "entity2": "Ecology", "relationship": "has subtopic"},
    {"entity1": "Biology", "entity2": "Microbiology", "relationship": "has subtopic"},
    {"entity1": "Biology", "entity2": "Molecular Biology", "relationship": "has subtopic"},
    {"entity1": "Biology", "entity2": "Physiology", "relationship": "has subtopic"},
    {"entity1": "Biology", "entity2": "Botany", "relationship": "has subtopic"},
    {"entity1": "Biology", "entity2": "Zoology", "relationship": "has subtopic"},
    {"entity1": "Biology", "entity2": "Biotechnology", "relationship": "has subtopic"},
    {"entity1": "Chemistry", "entity2": "Organic Chemistry", "relationship": "has subtopic"},
    {"entity1": "Chemistry", "entity2": "Inorganic Chemistry", "relationship": "has subtopic"},
    {"entity1": "Chemistry", "entity2": "Physical Chemistry", "relationship": "has subtopic"},
    {"entity1": "Chemistry", "entity2": "Analytical Chemistry", "relationship": "has subtopic"},
    {"entity1": "Chemistry", "entity2": "Biochemistry", "relationship": "has subtopic"},
    {"entity1": "Chemistry", "entity2": "Theoretical Chemistry", "relationship": "has subtopic"},
    {"entity1": "Chemistry", "entity2": "Materials Science", "relationship": "has subtopic"},
    {"entity1": "Chemistry", "entity2": "Environmental Chemistry", "relationship": "has subtopic"},
    {"entity1": "Chemistry", "entity2": "Industrial Chemistry", "relationship": "has subtopic"},
    {"entity1": "Chemistry", "entity2": "Chemical Engineering", "relationship": "has subtopic"},
    {"entity1": "Business", "entity2": "Marketing", "relationship": "has subtopic"},
    {"entity1": "Business", "entity2": "Finance", "relationship": "has subtopic"},
    {"entity1": "Business", "entity2": "Management", "relationship": "has subtopic"},
    {"entity1": "Business", "entity2": "Entrepreneurship", "relationship": "has subtopic"},
    {"entity1": "Business", "entity2": "Human Resources", "relationship": "has subtopic"},
    {"entity1": "Business", "entity2": "Operations", "relationship": "has subtopic"},
    {"entity1": "Business", "entity2": "Supply Chain Management", "relationship": "has subtopic"},
    {"entity1": "Business", "entity2": "Business Strategy", "relationship": "has subtopic"},
    {"entity1": "Business", "entity2": "E-commerce", "relationship": "has subtopic"},
    {"entity1": "Business", "entity2": "Corporate Governance", "relationship": "has subtopic"},
    {"entity1": "Psychology", "entity2": "Cognitive Psychology", "relationship": "has subtopic"},
    {"entity1": "Psychology", "entity2": "Developmental Psychology", "relationship": "has subtopic"},
    {"entity1": "Psychology", "entity2": "Social Psychology", "relationship": "has subtopic"},
    {"entity1": "Psychology", "entity2": "Clinical Psychology", "relationship": "has subtopic"},
    {"entity1": "Psychology", "entity2": "Neuroscience", "relationship": "has subtopic"},
    {"entity1": "Psychology", "entity2": "Behavioral Psychology", "relationship": "has subtopic"},
    {"entity1": "Psychology", "entity2": "Personality Psychology", "relationship": "has subtopic"},
    {"entity1": "Psychology", "entity2": "Industrial-Organizational Psychology", "relationship": "has subtopic"},
    {"entity1": "Psychology", "entity2": "Forensic Psychology", "relationship": "has subtopic"},
    {"entity1": "Psychology", "entity2": "Health Psychology", "relationship": "has subtopic"},
    {"entity1": "Literature", "entity2": "Poetry", "relationship": "has subtopic"},
    {"entity1": "Literature", "entity2": "Fiction", "relationship": "has subtopic"},
    {"entity1": "Literature", "entity2": "Non-fiction", "relationship": "has subtopic"},
    {"entity1": "Literature", "entity2": "Drama", "relationship": "has subtopic"},
    {"entity1": "Literature", "entity2": "Literary Theory", "relationship": "has subtopic"},
    {"entity1": "Literature", "entity2": "Comparative Literature", "relationship": "has subtopic"},
    {"entity1": "Literature", "entity2": "Narrative", "relationship": "has subtopic"},
    {"entity1": "Literature", "entity2": "Postmodernism", "relationship": "has subtopic"},
    {"entity1": "Literature", "entity2": "Symbolism", "relationship": "has subtopic"},
    {"entity1": "Literature", "entity2": "Literary Criticism", "relationship": "has subtopic"},
    {"entity1": "Economics", "entity2": "Microeconomics", "relationship": "has subtopic"},
    {"entity1": "Economics", "entity2": "Macroeconomics", "relationship": "has subtopic"},
    {"entity1": "Economics", "entity2": "Behavioral Economics", "relationship": "has subtopic"},
    {"entity1": "Economics", "entity2": "Development Economics", "relationship": "has subtopic"},
    {"entity1": "Economics", "entity2": "International Economics", "relationship": "has subtopic"},
    {"entity1": "Economics", "entity2": "Labor Economics", "relationship": "has subtopic"},
    {"entity1": "Economics", "entity2": "Public Economics", "relationship": "has subtopic"},
    {"entity1": "Economics", "entity2": "Environmental Economics", "relationship": "has subtopic"},
    {"entity1": "Economics", "entity2": "Game Theory", "relationship": "has subtopic"},
    {"entity1": "Economics", "entity2": "Econometrics", "relationship": "has subtopic"},
    {"entity1": "Ethics", "entity2": "Normative Ethics", "relationship": "has subtopic"},
    {"entity1": "Ethics", "entity2": "Meta-Ethics", "relationship": "has subtopic"},
    {"entity1": "Ethics", "entity2": "Applied Ethics", "relationship": "has subtopic"},
    {"entity1": "Ethics", "entity2": "Bioethics", "relationship": "has subtopic"},
    {"entity1": "Ethics", "entity2": "Environmental Ethics", "relationship": "has subtopic"},
    {"entity1": "Ethics", "entity2": "Business Ethics", "relationship": "has subtopic"},
    {"entity1": "Ethics", "entity2": "Virtue Ethics", "relationship": "has subtopic"},
    {"entity1": "Ethics", "entity2": "Deontological Ethics", "relationship": "has subtopic"},
    {"entity1": "Ethics", "entity2": "Consequentialism", "relationship": "has subtopic"},
    {"entity1": "Ethics", "entity2": "Social Ethics", "relationship": "has subtopic"},
    {"entity1": "Politics", "entity2": "Political Theory", "relationship": "has subtopic"},
    {"entity1": "Politics", "entity2": "Comparative Politics", "relationship": "has subtopic"},
    {"entity1": "Politics", "entity2": "International Relations", "relationship": "has subtopic"},
    {"entity1": "Politics", "entity2": "Public Policy", "relationship": "has subtopic"},
    {"entity1": "Politics", "entity2": "Political Economy", "relationship": "has subtopic"},
    {"entity1": "Politics", "entity2": "Political Institutions", "relationship": "has subtopic"},
    {"entity1": "Politics", "entity2": "Political Behavior", "relationship": "has subtopic"},
    {"entity1": "Politics", "entity2": "Global Governance", "relationship": "has subtopic"},
    {"entity1": "Politics", "entity2": "Political Ideologies", "relationship": "has subtopic"},
    {"entity1": "Politics", "entity2": "Conflict Studies", "relationship": "has subtopic"},
    {"entity1": "Art", "entity2": "Visual Arts", "relationship": "has subtopic"},
    {"entity1": "Art", "entity2": "Performing Arts", "relationship": "has subtopic"},
    {"entity1": "Art", "entity2": "Literary Arts", "relationship": "has subtopic"},
    {"entity1": "Art", "entity2": "Art History", "relationship": "has subtopic"},
    {"entity1": "Art", "entity2": "Art Theory", "relationship": "has subtopic"},
    {"entity1": "Art", "entity2": "Contemporary Art", "relationship": "has subtopic"},
    {"entity1": "Art", "entity2": "Art Criticism", "relationship": "has subtopic"},
    {"entity1": "Art", "entity2": "Sculpture", "relationship": "has subtopic"},
    {"entity1": "Art", "entity2": "Photography", "relationship": "has subtopic"},
    {"entity1": "Art", "entity2": "Installation Art", "relationship": "has subtopic"},
    {"entity1": "The Brain", "entity2": "Mathematics", "relationship": "related to"},
    {"entity1": "The Brain", "entity2": "Computer Science", "relationship": "related to"},
    {"entity1": "The Brain", "entity2": "Physics", "relationship": "related to"},
    {"entity1": "The Brain", "entity2": "Biology", "relationship": "related to"},
    {"entity1": "The Brain", "entity2": "Chemistry", "relationship": "related to"},
    {"entity1": "The Brain", "entity2": "Business", "relationship": "related to"},
    {"entity1": "The Brain", "entity2": "Psychology", "relationship": "related to"},
    {"entity1": "The Brain", "entity2": "Literature", "relationship": "related to"},
    {"entity1": "The Brain", "entity2": "Economics", "relationship": "related to"},
    {"entity1": "The Brain", "entity2": "Ethics", "relationship": "related to"},
    {"entity1": "The Brain", "entity2": "Politics", "relationship": "related to"},
    {"entity1": "The Brain", "entity2": "Art", "relationship": "related to"}
]
"""