# __init__.py

from flask import Flask
from app.routes import main_bp  # Import the main blueprint for routing

def create_app():
    app = Flask(__name__)  

    # Load configuration from config.py or environment variables
    app.config.from_object('config')

    # Register blueprints for modular routing
    app.register_blueprint(main_bp)

    return app