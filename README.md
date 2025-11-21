# simple-notes-application-175021-175030

This workspace contains a FastAPI backend for a simple notes application.

- Backend service: notes_backend
- API Docs (when running locally): http://localhost:3001/docs
- Export OpenAPI (canonical):
  - From the notes_backend directory run:
    - `python -m src.api.export_openapi`
    - Or if PYTHONPATH is not set: `PYTHONPATH=./ python -m src.api.export_openapi`
  - Output file: notes_backend/interfaces/openapi.json

Note: A legacy shim `src/api/generate_openapi.py` is provided for backward compatibility and delegates to `src.api.export_openapi`. Prefer using `export_openapi`.