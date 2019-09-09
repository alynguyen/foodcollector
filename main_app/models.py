from django.db import models

class Food(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  comments = models.CharField(max_length=250)
  rating = models.IntegerField()
