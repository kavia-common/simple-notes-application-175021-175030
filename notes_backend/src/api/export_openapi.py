"""
Utility script to export the FastAPI OpenAPI schema to interfaces/openapi.json.

This script imports the FastAPI app from src.api.main and writes the current
OpenAPI schema to the interfaces/openapi.json file in the container root. Use
this to keep interface contracts in sync with the code.

Usage:
  python -m src.api.export_openapi

Environment:
  - No environment variables are required. The script writes to a relative
    path within the container directory structure.

Notes:
  - This script does not start a server; it generates the schema directly
    from the FastAPI app instance.
  - The generated JSON is formatted with indentation for readability.
"""

import json
import os
from pathlib import Path
from typing import Any, Dict

from .main import app


def _resolve_interfaces_path() -> Path:
    """
    Resolve the output path for interfaces/openapi.json relative to this file's location.
    """
    # This file is in notes_backend/src/api/export_openapi.py
    # We want notes_backend/interfaces/openapi.json
    current = Path(__file__).resolve()
    backend_root = current.parents[2]  # notes_backend/
    interfaces_dir = backend_root / "interfaces"
    interfaces_dir.mkdir(parents=True, exist_ok=True)
    return interfaces_dir / "openapi.json"


# PUBLIC_INTERFACE
def generate_openapi_dict() -> Dict[str, Any]:
    """Generate the OpenAPI spec dictionary from the FastAPI app."""
    return app.openapi()


# PUBLIC_INTERFACE
def export_openapi_to_file(out_path: Path | None = None) -> Path:
    """Export the OpenAPI spec to a JSON file and return the output path."""
    if out_path is None:
        out_path = _resolve_interfaces_path()

    spec = generate_openapi_dict()

    # Write JSON with readability
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)

    return out_path


def _main() -> int:
    """CLI entrypoint for exporting the OpenAPI file."""
    out_path = export_openapi_to_file()
    print(f"OpenAPI spec exported to: {out_path}")
    return os.EX_OK


if __name__ == "__main__":
    raise SystemExit(_main())
