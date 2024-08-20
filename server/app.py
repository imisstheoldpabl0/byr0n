import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify
# from flask_cors import CORS

CREATE_USERS_TABLE = (
    """CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username VARCHAR);"""
)

INSERT_USER = (
    """INSERT INTO users (username) VALUES (%s);"""
)

load_dotenv()

# Creates the app instance
app = Flask(__name__)

# Access the .env file to obtain the DB URL
url = os.getenv("DATABASE_URL")

# Connect to Postgres DB with psycopg2 and pass URL
connection = psycopg2.connect(url)

# Allow Cross-Origin
# cors = CORS(app, origins='*')

@app.get("/")
def home():
    return "<h1>Hello world</h1>"

""" @app.post("/api/user")
def create_user():
    data = request.get_json()
    username = data["username"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_USER, (username))
    return {"message": f"user created with username: {username}"}, 201 """

@app.route("/api/user", methods=['POST'])
def post_user():
    if request.is_json:
        data = request.get_json()
        username = data.username
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(INSERT_USER, (username,))
        return jsonify(data), 200
    else:
        return jsonify({"error": "Invalid content type"}), 400

@app.route('/post_json', methods=['POST'])
def post_json():
    # Check if the request content type is JSON
    if request.is_json:
        data = request.get_json()  # Parse the JSON data
        response = {
            "message": "JSON received!",
            "data": data
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Invalid content type"}), 400
    
    
if __name__ == "__main__":
    app.run(debug=True, port=8080)