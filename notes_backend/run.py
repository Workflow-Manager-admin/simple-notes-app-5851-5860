"""Entry point for running the Notes Flask API server.

Usage:
    python run.py

Environment:
    Configuration is read from .env file (DATABASE_URL for DB, etc.)

API Endpoints:
    - POST    /notes         : Create a new note
    - GET     /notes         : List all notes
    - GET     /notes/<id>    : Get a specific note by id
    - PUT     /notes/<id>    : Update a note by id
    - DELETE  /notes/<id>    : Delete a note by id

Full OpenAPI docs at /docs/openapi.json or interactive Swagger UI at /docs
"""

from app import app

if __name__ == "__main__":
    # By default runs on http://127.0.0.1:5000
    app.run()
