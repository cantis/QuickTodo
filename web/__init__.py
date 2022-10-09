from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ

# global objects
db = SQLAlchemy()


def create_app() -> Flask:
    '''Create Flask App and configure it'''
    # This is called the create_app factory pattern you can read more about it here:
    # https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/

    # Create the Flask app
    app = Flask(__name__)

    # Load environment variables from .env file
    load_dotenv()

    # Configure the app from environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    # Connect Routes
    from web.routes import home

    # Register the blueprints
    app.register_blueprint(home.bp)

    # Create the database tables
    with app.app_context():
        db.create_all()

    # Return the app instance
    return app
