from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex


# Create your models here.
class Quote(models.Model):
    name = models.CharField(max_length=250)
    quote = models.TextField(max_length=1000)
    search_vector = SearchVectorField(null=True)

    def __str__(self):
        return self.quote

    class Meta:
        indexes = [
            GinIndex(fields=["search_vector"]),
        ]
