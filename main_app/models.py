from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Food(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  comments = models.CharField(max_length=250)
  rating = models.IntegerField()

  def get_absolute_url(self):
    return reverse('details', kwargs={'food_id': self.id})

class Review(models.Model):
  user = models.CharField(max_length=100)
  review = models.CharField(max_length=250)
  rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
  food = models.ForeignKey(Food, on_delete=models.CASCADE)