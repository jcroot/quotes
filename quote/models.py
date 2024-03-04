from django.db import models


class AuthorManager(models.Manager):

    def getFourRandomAuthors(self, author_id):
        authors = self.exclude(id=author_id).order_by('?')[:3]
        return list(authors) + [self.get(id=author_id)]


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AuthorManager()


class QuoteManager(models.Manager):

    def getRandomQuote(self):
        return self.get_queryset().order_by('?').first()


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, related_name="quotes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = QuoteManager()

    def __str__(self):
        return self.quote

    def author_name(self):
        return self.author.name
