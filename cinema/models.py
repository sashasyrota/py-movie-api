from django.db import models


class Movie(models.Model):
    title = models.CharField()
    description = models.TextField()
    duration = models.IntegerField()
