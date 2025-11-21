# Notes Backend (FastAPI)

This service exposes a simple REST API for creating, reading, updating, and deleting notes. It uses an in-memory, thread-safe repository (no external database) and is intended for demo and development purposes.

## Run

- Install dependencies:
  pip install -r requirements.txt

- Start server on port 3001:
  uvicorn src.api.main:app --host 0.0.0.0 --port 3001 --reload

- Open the interactive API docs (Swagger UI):
  http://localhost:3001/docs

## Regenerate OpenAPI spec

To export the current OpenAPI spec used by this backend into interfaces/openapi.json, run the single export script:

- Using module (canonical):
  python -m src.api.export_openapi

- Or if PYTHONPATH isn't set, run from the notes_backend directory:
  PYTHONPATH=./ python -m src.api.export_openapi

The file will be written to:
notes_backend/interfaces/openapi.json

Backward compatibility:
- A deprecated shim may exist at `src/api/generate_openapi.py` which simply delegates to `export_openapi`. Prefer using `src.api.export_openapi`.

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
