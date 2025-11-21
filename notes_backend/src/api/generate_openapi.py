"""
Deprecated shim: delegates to src.api.export_openapi for exporting the OpenAPI schema.

Prefer running:
  python -m src.api.export_openapi
"""

# PUBLIC_INTERFACE
def main() -> int:
    """Deprecated entrypoint that delegates to export_openapi._main()."""
    # Deferred import to avoid any circular import issues at module import time.
    from .export_openapi import _main as _export_main
    return _export_main()


if __name__ == "__main__":
    raise SystemExit(main())
