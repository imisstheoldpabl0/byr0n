from flask import Blueprint, request, jsonify
from db import connection  # Import the connection from db.py
import queries


# Create a blueprint for your routes
routes = Blueprint('routes', __name__)

@routes.route("/", methods=['GET'])
def home():
    return "Hello world"

@routes.route("/api/user", methods=['GET'])
def get_users():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.GET_USERS_IN_DB)
            user_data = cursor.fetchall()
    # return jsonify({"message": f"all users returned: {user_data}"})
    return jsonify({"data": user_data})

@routes.route("/api/user", methods=['DELETE'])
def delete_users():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(queries.DELETE_ALL_USERS_IN_DB)
    return jsonify({"message": "all users deleted"})

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
            cursor.execute(queries.INSERT_USER_RETURN_ID, (username, email, password, login_status))
            user_id = cursor.fetchone()[0]

    return jsonify({"message": f"User created with username: {username}", "user_id": user_id}), 201
