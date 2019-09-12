from django.contrib import admin
from .models import Food, Review, Photo, Category

# Register your models here.
admin.site.register(Food)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Photo)