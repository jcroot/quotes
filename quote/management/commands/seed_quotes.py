from django.core.management import BaseCommand
import requests


class Command(BaseCommand):
    help = "This command seeds the database with authors and quotes"

    def handle(self, *args, **options):
        from quote.models import Quote

        response = requests.get("https://www.scalablepath.com/api/test/test-quotes")
        quotes = response.json()
        for quote in quotes:
            Quote.objects.create(quote=quote.get('quote'), author_id=quote.get('author_id'))

        self.stdout.write(self.style.SUCCESS("Database seeded successfully"))
