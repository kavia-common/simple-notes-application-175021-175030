"""
Deprecated shim: use src.api.export_openapi instead.

This module exists for backward compatibility only. It delegates to the
exporter in src.api.export_openapi so that legacy commands like:

  python -m src.api.generate_openapi

continue to work. Preferred usage:

  python -m src.api.export_openapi
"""
from .export_openapi import _main as _delegate_main

if __name__ == "__main__":
    raise SystemExit(_delegate_main())
