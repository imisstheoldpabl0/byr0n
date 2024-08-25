from flask import Blueprint, request, jsonify, session
from db import connection  # Import the connection from db.py
import queries
import uuid


# Create a blueprint for your routes
routes = Blueprint('routes', __name__)

# **: Home route
@routes.route("/", methods=['GET'])
def home():
    return "Hello world"

# ADMIN: Get all users
@routes.route("/api/user", methods=['GET'])
def get_users():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.GET_USERS_IN_DB)
            user_data = cursor.fetchall()
    # return jsonify({"message": f"all users returned: {user_data}"})
    return jsonify({"data": user_data})

# **: Delete all users
@routes.route("/api/user", methods=['DELETE'])
def delete_users():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.DELETE_ALL_USERS_IN_DB)
    return jsonify({"message": "all users deleted"})

# **: Create new user
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
            cursor.execute(queries.CREATE_USERS_TABLE)
            
            cursor.execute(queries.CHECK_USER_IN_DB, (username, email))
            existing_user = cursor.fetchone()
            
            if existing_user:
                return jsonify({"error": "Username or email already exists"}), 409
            
            
            cursor.execute(queries.INSERT_USER_RETURN_ID, (username, email, password, login_status))
            user_id = cursor.fetchone()[0]

    return jsonify({"message": f"User created with username: {username}", "user_id": user_id}), 201

# **: Login user
@routes.route("/api/login", methods=['PUT'])
def login_user():
    data = request.get_json()
    
    required_fields = ["username", "password"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Username and password are required"}), 400
    
    username = data["username"]
    password = data["password"]
    
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.UPDATE_LOGIN_STATUS, (username, password))
            user_id = cursor.fetchone()
        
        if user_id:
            session_token = str(uuid.uuid4())

            session['user_id'] = user_id[0]
            session['session_token'] = session_token
            
            return jsonify({
                "message": f"User {username} logged in successfully",
                "user_id": user_id[0],
                "session_token": session_token
            }), 200
            
        else:
            return jsonify({"error": "Invalid username or password"}), 401