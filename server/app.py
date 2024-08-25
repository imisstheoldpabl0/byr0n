from flask import Flask
from routes import routes
from flask_cors import CORS

# Create the app instance
app = Flask(__name__)

CORS(app)

app.secret_key = 'hello123'

# Register the blueprint
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
