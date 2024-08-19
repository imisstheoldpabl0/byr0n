import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Create a connection to the database
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
