from django.db import models


class AuthorManager(models.Manager):

    def getFourRandomAuthors(self):
        return self.get_queryset().order_by('?')[:4]


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
