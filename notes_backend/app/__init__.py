from flask import Flask
from flask_cors import CORS
from .routes.health import blp as health_blp
from flask_smorest import Api
from .models import db
from .routes.notes import blp as notes_blp
import os
from dotenv import load_dotenv

# Load .env variables (allowing for DB config changes in the future)
base_dir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(base_dir, '..', '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

def create_app():
    """Application factory for Flask Notes API."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config["API_TITLE"] = "My Flask API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config['OPENAPI_URL_PREFIX'] = '/docs'
    app.config["OPENAPI_SWAGGER_UI_PATH"] = ""
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # Database Config: use SQLite file in project directory by default
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL",
        "sqlite:///notes.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    api = Api(app)
    api.register_blueprint(health_blp)
    api.register_blueprint(notes_blp)

    with app.app_context():
        db.create_all()

    return app

# For backwards compatibility & "flask run" CLI
app = create_app()
