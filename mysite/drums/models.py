from django.db import models

class Cover(models.Model):
    genre = models.CharField(max_length = 255)
    url = models.CharField(max_length = 255)
