# simple-notes-application-175021-175030

This workspace contains a FastAPI backend for a simple notes application.

- Backend service: notes_backend
- API Docs (when running locally): http://localhost:3001/docs
- Export OpenAPI: from the notes_backend directory run:
  - `python -m src.api.export_openapi` (or `PYTHONPATH=./ python -m src.api.export_openapi` if PYTHONPATH is not set)
  - Output file: notes_backend/interfaces/openapi.json