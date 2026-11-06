# ORCA repository

Rules for building UIs with ORCA: see AGENTS.md.

Working on ORCA itself:
- Tokens live in `orca/tokens.py`; elements in `orca/catalogue/`. After any change run `.venv/bin/python -m orca build`.
- Tests: `.venv/bin/python -m django test tests --settings=tests.settings`.
- Never edit generated files (`orca/static/orca/css/tokens.css`, `docs/primitives/`, `docs/catalogue.json`).
