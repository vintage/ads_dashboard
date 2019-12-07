import os

from django.core.management.base import BaseCommand
from django.conf import settings

from ads import parser

INITIAL_DATA_FILE = os.path.join(settings.BASE_DIR, "ads/data/initial.csv")


class Command(BaseCommand):
    help = "Loads initial stats data from local file"

    def handle(self, *args, **options):
        with open(INITIAL_DATA_FILE) as initial_file:
            parser_items = parser.parse_file(initial_file)
            parser.save_items(parser_items)

            self.stdout.write(
                self.style.SUCCESS(f"Successfully imported stats objects")
            )
