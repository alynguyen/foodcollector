from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('foods/', views.food_index, name='index'),
   path('foods/<int:food_id>', views.food_details, name='details'),
   path('foods/create/', views.FoodCreate.as_view(), name='food_create'),
   path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='food_update'),
   path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='food_delete'),
   path('foods/<int:food_id>/add_review/', views.add_review, name='add_review'),
   path('foods/<int:food_id>/delete_review/', views.delete_review, name='delete_review'),
   path('foods/<int:pk>/delete/', views.ReviewDelete.as_view(), name='review_delete'),
]