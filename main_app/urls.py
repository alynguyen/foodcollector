from django.urls import path

from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('foods/', views.food_index, name='index'),
   path('foods/<int:food_id>', views.food_details, name='details'),
]