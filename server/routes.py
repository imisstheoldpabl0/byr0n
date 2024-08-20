from flask import Blueprint, request, jsonify
from db import connection  # Import the connection from db.py


# Create a blueprint for your routes
routes = Blueprint('routes', __name__)

CREATE_USERS_TABLE = (
    """CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR,
        email VARCHAR,
        password VARCHAR,
        login_status BOOLEAN DEFAULT FALSE
    );"""
)

INSERT_USER_RETURN_ID = (
    """INSERT INTO users (username, email, password, login_status) 
       VALUES (%s, %s, %s, %s) RETURNING id;"""
)

GET_USERS_IN_DB = (
    """SELECT * FROM users"""
)

@routes.route("/", methods=['GET'])
def home():
    return "Hello world"

@routes.route("/api/user", methods=['GET'])
def get_users():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_USERS_IN_DB)
    return jsonify({"message": "all users returned"})

@routes.route("/api/user", methods=['POST'])
def create_user():
    data = request.get_json()
    
    required_fields = ["username", "email", "password", "login_status"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Invalid input, all fields are required"}), 400

    username = data["username"]
    email = data["email"]
    password = data["password"]
    login_status = data["login_status"]

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(INSERT_USER_RETURN_ID, (username, email, password, login_status))
            user_id = cursor.fetchone()[0]

    return jsonify({"message": f"User created with username: {username}", "user_id": user_id}), 201
