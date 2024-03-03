from django.core.management import BaseCommand
import requests


class Command(BaseCommand):
    help = "This command seeds the database with authors"

    def handle(self, *args, **options):
        from quote.models import Author

        response = requests.get("https://www.scalablepath.com/api/test/test-authors")
        authors = response.json()
        for author in authors:
            Author.objects.create(id=author.get('id'), name=author.get('name'))

        self.stdout.write(self.style.SUCCESS("Database seeded successfully"))
