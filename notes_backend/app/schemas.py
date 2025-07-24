"""Marshmallow schemas for Notes API (for validation & serialization)."""

from marshmallow import Schema, fields

# PUBLIC_INTERFACE
class NoteSchema(Schema):
    """Schema for full Note serialization and validation."""
    id = fields.String(dump_only=True, description="The unique ID for the note (uuid).")
    title = fields.String(required=True, description="The title of the note.")
    content = fields.String(required=True, description="The content of the note.")
    timestamp = fields.DateTime(dump_only=True, description="The timestamp of the note.")

# For POST (input) -- don't require id, nor timestamp
# For PATCH/PUT (update) you may require at least title/content, but not id/timestamp
