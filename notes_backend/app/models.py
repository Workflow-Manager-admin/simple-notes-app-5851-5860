"""Models and database setup for Notes application."""

import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from uuid import uuid4

from dotenv import load_dotenv

# Load environment variables from .env
base_dir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(base_dir, '..', '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

db = SQLAlchemy()


# PUBLIC_INTERFACE
class Note(db.Model):
    """SQLAlchemy model for a Note object."""
    __tablename__ = 'notes'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, server_default=func.now(), default=datetime.utcnow)

    def to_dict(self):
        """Serialize Note object to dict."""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp.isoformat()
        }
