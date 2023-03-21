from django.conf import settings
from django.db import models
class Event(models.Model):
    'Generated Model'
    title = models.CharField(max_length=256,)
    date = models.DateTimeField()
