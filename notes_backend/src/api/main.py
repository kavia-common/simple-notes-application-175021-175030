from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.notes import router as notes_router

openapi_tags = [
    {
        "name": "notes",
        "description": "Operations related to notes CRUD.",
    }
]

app = FastAPI(
    title="Simple Notes API",
    description="A minimal FastAPI backend providing CRUD operations for notes using an in-memory repository.",
    version="0.1.0",
    openapi_tags=openapi_tags,
)

# Enable permissive CORS for demo purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", summary="Health Check", tags=["health"])
def health_check():
    """Return basic health status for the service."""
    return {"message": "Healthy"}


# Mount notes router under /api
app.include_router(notes_router, prefix="/api")
