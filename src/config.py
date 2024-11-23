import os
from dotenv import load_dotenv
from py2neo import Graph

# Load environment variables
load_dotenv()

# Set up API and database credentials
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

def initialize_neo4j_connection():
    """Initialize a connection to the Neo4j database."""
    return Graph(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

