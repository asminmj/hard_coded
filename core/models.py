from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField('time', default=timezone.now)

    def __str__(self):
        return self.name
