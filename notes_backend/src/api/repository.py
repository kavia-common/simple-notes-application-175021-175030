from __future__ import annotations

from datetime import datetime, timezone
from threading import Lock
from typing import Dict, List, Optional

from .schemas import Note, NoteCreate, NoteUpdate


class InMemoryNotesRepository:
    """Thread-safe in-memory repository implementation for notes.

    Stores notes in a dictionary with auto-incrementing integer IDs.
    All write operations are protected by a threading.Lock to ensure thread-safety.
    """

    def __init__(self) -> None:
        self._notes: Dict[int, Note] = {}
        self._lock = Lock()
        self._next_id: int = 1

    def _now(self) -> datetime:
        """Return a timezone-aware UTC datetime for consistent serialization."""
        return datetime.now(timezone.utc)

    # PUBLIC_INTERFACE
    def create_note(self, data: NoteCreate) -> Note:
        """Create a new note, assigning an auto-incremented ID."""
        with self._lock:
            note_id = self._next_id
            self._next_id += 1

            now = self._now()
            note = Note(
                id=note_id,
                title=data.title,
                content=data.content,
                created_at=now,
                updated_at=now,
            )
            self._notes[note_id] = note
            return note

    # PUBLIC_INTERFACE
    def list_notes(self, skip: int = 0, limit: int = 100) -> List[Note]:
        """Return a paginated list of notes."""
        # Reads can be done without lock if immutability is guaranteed,
        # but to be safe with potential concurrent writes, use lock.
        with self._lock:
            all_notes = list(self._notes.values())
            # Stable ordering by id
            all_notes.sort(key=lambda n: n.id)
            return all_notes[skip : skip + limit]

    # PUBLIC_INTERFACE
    def get_note(self, note_id: int) -> Optional[Note]:
        """Retrieve a single note by id, or None if not found."""
        with self._lock:
            return self._notes.get(note_id)

    # PUBLIC_INTERFACE
    def update_note(self, note_id: int, data: NoteUpdate) -> Optional[Note]:
        """Update a note with provided fields. Returns updated note or None if not found."""
        with self._lock:
            if note_id not in self._notes:
                return None
            existing = self._notes[note_id]
            updated = existing.model_copy(
                update={
                    "title": data.title if data.title is not None else existing.title,
                    "content": data.content if data.content is not None else existing.content,
                    "updated_at": self._now(),
                }
            )
            self._notes[note_id] = updated
            return updated

    # PUBLIC_INTERFACE
    def replace_note(self, note_id: int, data: NoteCreate) -> Optional[Note]:
        """Replace a note entirely (PUT semantics). Returns replaced note or None if not found."""
        with self._lock:
            if note_id not in self._notes:
                return None
            existing = self._notes[note_id]
            now = self._now()
            replacement = Note(
                id=note_id,
                title=data.title,
                content=data.content,
                created_at=existing.created_at,
                updated_at=now,
            )
            self._notes[note_id] = replacement
            return replacement

    # PUBLIC_INTERFACE
    def delete_note(self, note_id: int) -> bool:
        """Delete a note by id. Returns True if it existed and was deleted."""
        with self._lock:
            if note_id in self._notes:
                del self._notes[note_id]
                return True
            return False


# Singleton-style repository instance for app-wide use.
repo = InMemoryNotesRepository()
