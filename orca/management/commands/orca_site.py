from django.core.management.base import BaseCommand

from ...site import export


class Command(BaseCommand):
    help = "Export the ORCA documentation website as static HTML (one file per page, relative links)."

    def add_arguments(self, parser):
        parser.add_argument("out_dir", nargs="?", default="site", help="Output folder (replaced). Default: site")
        parser.add_argument("--fragment-index", action="store_true",
                            help="Write index.html without its document wrapper, for hosts that add their own.")

    def handle(self, *args, **opts):
        files = export(opts["out_dir"], fragment_index=opts["fragment_index"])
        pages = sum(1 for f in files if f.suffix == ".html" and "static" not in f.parts)
        self.stdout.write(self.style.SUCCESS(f"Wrote {pages} pages and {len(files) - pages} other files to {opts['out_dir']}/"))
