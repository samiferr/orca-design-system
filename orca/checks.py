"""Django system checks for ORCA settings (run with `manage.py check` and at every runserver start)."""

from django.core import checks

from .conf import THEMES, compute_brand, user_settings

KNOWN_KEYS = {"BRAND", "THEME", "DOCS_ENABLED"}


@checks.register("orca")
def check_settings(app_configs=None, **kwargs):
    messages = []
    raw = user_settings()
    for key in raw:
        if key not in KNOWN_KEYS:
            messages.append(checks.Error(
                f"settings.ORCA has an unknown key {key!r}.",
                hint=f"Known keys: {', '.join(sorted(KNOWN_KEYS))}. Only brand tokens can be customised (ORCA['BRAND']).",
                id="orca.E001",
            ))
    theme = str(raw.get("THEME", "auto")).lower()
    if theme not in THEMES:
        messages.append(checks.Error(
            f"settings.ORCA['THEME'] is {raw.get('THEME')!r}.", hint=f"Use one of: {', '.join(THEMES)}.", id="orca.E003",
        ))
    brand = compute_brand()
    for error in brand.errors:
        messages.append(checks.Error(error, id="orca.E002"))
    for note in brand.notes:
        messages.append(checks.Warning(
            note, hint="ORCA adjusted a brand colour to keep text readable. Set the adjusted value to silence this.", id="orca.W001",
        ))
    return messages
