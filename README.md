# simple-notes-application-175021-175030

This workspace contains a FastAPI backend for a simple notes application with full CRUD for notes.

- Backend service: notes_backend

Run locally:
1) Install dependencies
   cd notes_backend
   pip install -r requirements.txt

2) Start the API server on port 3001
   uvicorn src.api.main:app --host 0.0.0.0 --port 3001 --reload

3) Open the interactive API docs
   http://localhost:3001/docs

OpenAPI export (canonical):
- From the notes_backend directory, write the OpenAPI schema to interfaces/openapi.json:
  python -m src.api.export_openapi
- Or if PYTHONPATH is not set:
  PYTHONPATH=./ python -m src.api.export_openapi
- Output file:
  notes_backend/interfaces/openapi.json

Note: A legacy shim `src/api/generate_openapi.py` may exist for backward compatibility and delegates to `src.api.export_openapi`. Prefer using `export_openapi`.