from typing import List

from fastapi import APIRouter, HTTPException, Path, Query, status

from ..repository import repo
from ..schemas import Note, NoteCreate, NoteUpdate

router = APIRouter(
    tags=["notes"],
)


@router.post(
    "/notes",
    status_code=status.HTTP_201_CREATED,
    response_model=Note,
    summary="Create a note",
    description="Create a new note with a title and content.",
    responses={
        201: {"description": "Note created successfully"},
        422: {"description": "Validation error"},
    },
)
# PUBLIC_INTERFACE
def create_note(payload: NoteCreate) -> Note:
    """Create a new note and return it."""
    return repo.create_note(payload)


@router.get(
    "/notes",
    response_model=List[Note],
    summary="List notes",
    description="List notes with optional pagination using skip and limit parameters.",
)
# PUBLIC_INTERFACE
def list_notes(
    skip: int = Query(0, ge=0, description="Number of records to skip for pagination"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
) -> List[Note]:
    """Return a paginated list of notes."""
    return repo.list_notes(skip=skip, limit=limit)


@router.get(
    "/notes/{note_id}",
    response_model=Note,
    summary="Get a note",
    description="Retrieve a single note by its ID.",
    responses={404: {"description": "Note not found"}},
)
# PUBLIC_INTERFACE
def get_note(
    note_id: int = Path(..., ge=1, description="ID of the note to retrieve"),
) -> Note:
    """Retrieve a single note by ID, or raise 404 if not found."""
    note = repo.get_note(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put(
    "/notes/{note_id}",
    response_model=Note,
    summary="Replace a note",
    description="Replace an existing note's title and content. All fields are required.",
    responses={404: {"description": "Note not found"}},
)
# PUBLIC_INTERFACE
def replace_note(
    payload: NoteCreate,
    note_id: int = Path(..., ge=1, description="ID of the note to replace"),
) -> Note:
    """Replace an existing note using PUT semantics. 404 if note does not exist."""
    note = repo.replace_note(note_id, payload)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.patch(
    "/notes/{note_id}",
    response_model=Note,
    summary="Update a note",
    description="Partially update fields of an existing note.",
    responses={404: {"description": "Note not found"}},
)
# PUBLIC_INTERFACE
def update_note(
    payload: NoteUpdate,
    note_id: int = Path(..., ge=1, description="ID of the note to update"),
) -> Note:
    """Partially update an existing note. 404 if note does not exist."""
    note = repo.update_note(note_id, payload)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.delete(
    "/notes/{note_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a note",
    description="Delete a note by its ID.",
    responses={404: {"description": "Note not found"}},
)
# PUBLIC_INTERFACE
def delete_note(
    note_id: int = Path(..., ge=1, description="ID of the note to delete"),
) -> None:
    """Delete a note by ID. Returns 204 on success, 404 if the note does not exist."""
    ok = repo.delete_note(note_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Note not found")
    # 204 No Content requires no response body
    return None
