# Notes Backend (FastAPI)

This service exposes a simple REST API for creating, reading, updating, and deleting notes. It uses an in-memory, thread-safe repository (no external database) and is intended for demo and development purposes.

## Run

- Install dependencies:
  pip install -r requirements.txt

- Start server:
  uvicorn src.api.main:app --host 0.0.0.0 --port 3001 --reload

- Open API docs:
  http://localhost:3001/docs

## Endpoints (prefixed with /api)

- POST /api/notes (201): Create a note
- GET /api/notes: List notes (?skip=&limit=)
- GET /api/notes/{note_id}: Get a note
- PUT /api/notes/{note_id}: Replace a note (all fields)
- PATCH /api/notes/{note_id}: Update a note (partial)
- DELETE /api/notes/{note_id} (204): Delete a note

Health check (no prefix):
- GET / -> {"message": "Healthy"}

## Data Models

- NoteBase: title (str), content (str)
- NoteCreate: NoteBase
- NoteUpdate: title (Optional[str]), content (Optional[str])
- Note: id (int), title (str), content (str), created_at (datetime), updated_at (datetime)
