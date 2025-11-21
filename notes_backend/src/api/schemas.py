from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


# PUBLIC_INTERFACE
class NoteBase(BaseModel):
    """Base note model with shared fields."""

    title: str = Field(..., description="Title of the note")
    content: str = Field(..., description="Content/body of the note")


# PUBLIC_INTERFACE
class NoteCreate(NoteBase):
    """Model for creating a new note."""
    pass


# PUBLIC_INTERFACE
class NoteUpdate(BaseModel):
    """Model for updating a note with partial fields allowed."""

    title: Optional[str] = Field(None, description="Updated title of the note")
    content: Optional[str] = Field(None, description="Updated content/body of the note")


# PUBLIC_INTERFACE
class Note(NoteBase):
    """Model returned by API representing a note resource."""

    id: int = Field(..., description="Unique identifier for the note")
    created_at: datetime = Field(..., description="Timestamp when the note was created")
    updated_at: datetime = Field(..., description="Timestamp when the note was last updated")
