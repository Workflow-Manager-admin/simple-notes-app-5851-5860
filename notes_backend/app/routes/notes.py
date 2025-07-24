"""Blueprint for Notes CRUD operations."""

from flask_smorest import Blueprint, abort
from flask.views import MethodView

from ..models import db, Note
from ..schemas import NoteSchema

blp = Blueprint(
    "Notes", "notes", url_prefix="/notes", description="CRUD operations on notes"
)

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)


@blp.route("/")
class NotesList(MethodView):
    """Handle creating and listing notes."""

    # PUBLIC_INTERFACE
    @blp.response(200, NoteSchema(many=True))
    def get(self):
        """List all notes. Returns 200 with an array of notes."""
        all_notes = Note.query.order_by(Note.timestamp.desc()).all()
        return notes_schema.dump(all_notes)

    # PUBLIC_INTERFACE
    @blp.arguments(NoteSchema)
    @blp.response(201, NoteSchema)
    def post(self, new_data):
        """Create a new note. Returns 201 and created note."""
        note = Note(
            title=new_data["title"],
            content=new_data["content"]
        )
        db.session.add(note)
        db.session.commit()
        return note_schema.dump(note), 201


@blp.route("/<string:note_id>")
class NoteById(MethodView):
    """Handle retrieving, updating, and deleting single notes."""

    # PUBLIC_INTERFACE
    @blp.response(200, NoteSchema)
    def get(self, note_id):
        """Get a note by id. Returns 200 with the note or 404 if not found."""
        note = Note.query.get(note_id)
        if not note:
            abort(404, message="Note not found")
        return note_schema.dump(note)

    # PUBLIC_INTERFACE
    @blp.arguments(NoteSchema)
    @blp.response(200, NoteSchema)
    def put(self, update_data, note_id):
        """Update a note by id (full update). Returns 200 when successful or 404 if not found."""
        note = Note.query.get(note_id)
        if not note:
            abort(404, message="Note not found")
        note.title = update_data["title"]
        note.content = update_data["content"]
        db.session.commit()
        return note_schema.dump(note)

    # PUBLIC_INTERFACE
    @blp.response(204)
    def delete(self, note_id):
        """Delete a note by id. Returns 204 if deleted, 404 if note not found."""
        note = Note.query.get(note_id)
        if not note:
            abort(404, message="Note not found")
        db.session.delete(note)
        db.session.commit()
        return '', 204
