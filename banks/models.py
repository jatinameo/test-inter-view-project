import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Bank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(unique=True)
    countries = ArrayField(models.TextField(), default=list, blank=True)

    def __str__(self):
        return self.name