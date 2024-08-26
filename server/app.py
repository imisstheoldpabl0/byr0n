import os
from dotenv import load_dotenv
from flask import Flask
from routes import routes
from flask_cors import CORS

from datetime import timedelta

load_dotenv()

# Create the app instance
app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

app.permanent_session_lifetime = timedelta(days=7)

CORS(app)


# Register the blueprint
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
