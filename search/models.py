from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Definition(models.Model):
    term = models.CharField(max_length=32, blank=False)
    definition = models.TextField(blank=False)
    aliases = ArrayField(models.CharField(max_length=32), blank=True)