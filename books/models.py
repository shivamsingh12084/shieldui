from __future__ import unicode_literals
from operator import mod
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)