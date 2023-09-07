from django.core.management import BaseCommand

from django_wordpress_import.importer.importer import Importer


class Command(BaseCommand):
    help = "Import WordPress data"

    def add_arguments(self, parser):
        parser.add_argument(
            "url",
            type=str,
            help="The url of the WordPress site json API.",
            default="",
        )
        parser.add_argument(
            "model",
            type=str,
            help="The model to import data to.",
        )

    def handle(self, *args, **options):
        importer = Importer(
            url=options["url"],
            model_name=options["model"],
        )
        importer.import_data()
