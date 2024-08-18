import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify

CREATE_USERS_TABLE = (
    """CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR);"""
)

INSERT_USER_RETURN_ID = (
    """INSERT INTO users (username) VALUES ('pablo');"""
)

load_dotenv()

# Creates the app instance
app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.route("/", methods=['GET'])
def home():
    return "Hello world"

@app.route("/api/user", methods=['POST'])
def create_user():
    data = request.get_json()
    username = data["username"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(INSERT_USER_RETURN_ID (username,))
    return {"message": f"User created with username: {username}"}, 201
    
    
if __name__ == "__main__":
    app.run(debug=True, port=8080)