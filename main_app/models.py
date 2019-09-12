from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
  name = models.CharField(max_length=20)
  description = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('index')

class Food(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  comments = models.CharField(max_length=250)
  rating = models.IntegerField()
  categories = models.ManyToManyField(Category)

  def get_absolute_url(self):
    return reverse('details', kwargs={'food_id': self.id})
  
  class Meta:
    ordering = ['-rating']

class Review(models.Model):
  user = models.CharField(max_length=100)
  review = models.CharField(max_length=250)
  rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
  food = models.ForeignKey(Food, on_delete=models.CASCADE)

class Photo(models.Model):
  url = models.CharField(max_length=200)
  food = models.ForeignKey(Food, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for food_id: {self.food_id} @{self.url}"