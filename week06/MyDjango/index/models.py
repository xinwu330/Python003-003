from django.db import models

# Create your models here.

class Review(models.Model):
    stars = models.SmallIntegerField()
    content = models.CharField(max_length=60)
    date = models.DateField()