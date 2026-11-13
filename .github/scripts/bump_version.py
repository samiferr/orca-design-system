"""Bump the ORCA version in pyproject.toml and orca/__init__.py, and print the new version.

Usage: python .github/scripts/bump_version.py [patch|minor|major]   (default: patch)
"""

import datetime
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PYPROJECT = ROOT / "pyproject.toml"
INIT = ROOT / "orca" / "__init__.py"


def bump(version: str, part: str) -> str:
    major, minor, patch = (int(n) for n in version.split("."))
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def main() -> None:
    part = sys.argv[1] if len(sys.argv) > 1 else "patch"
    if part not in {"patch", "minor", "major"}:
        sys.exit(f"Unknown bump type: {part}")

    pyproject = PYPROJECT.read_text()
    match = re.search(r'^version = "(\d+\.\d+\.\d+)"$', pyproject, re.M)
    if not match:
        sys.exit("Could not find a plain X.Y.Z version in pyproject.toml")
    new = bump(match.group(1), part)

    PYPROJECT.write_text(pyproject.replace(match.group(0), f'version = "{new}"', 1))

    init = INIT.read_text()
    init, n = re.subn(r'^__version__ = "[^"]+"', f'__version__ = "{new}"', init, flags=re.M)
    today = datetime.date.today()
    init, m = re.subn(
        r"^__released__ = _datetime\.date\([^)]*\)",
        f"__released__ = _datetime.date({today.year}, {today.month}, {today.day})",
        init,
        flags=re.M,
    )
    if n != 1 or m != 1:
        sys.exit("Could not update __version__/__released__ in orca/__init__.py")
    INIT.write_text(init)
    print(new)


if __name__ == "__main__":
    main()
