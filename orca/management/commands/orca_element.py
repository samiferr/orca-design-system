from django.core.management.base import BaseCommand, CommandError

from ...catalogue import registry
from ...catalogue.render import element_text


class Command(BaseCommand):
    help = "Print the why, when and how of an ORCA element (same as `python -m orca show <id>`)."

    def add_arguments(self, parser):
        parser.add_argument("element_id", nargs="?", help="Element id, e.g. button. Omit to list all ids.")

    def handle(self, *args, **opts):
        if not opts["element_id"]:
            for el in registry.all_elements():
                self.stdout.write(f"{el.id:<24} {el.name}")
            return
        el = registry.get(opts["element_id"])
        if el is None:
            hits = ", ".join(h.id for h in registry.search(opts["element_id"])[:8])
            raise CommandError(f"No element {opts['element_id']!r}." + (f" Did you mean: {hits}?" if hits else ""))
        self.stdout.write(element_text(el))
