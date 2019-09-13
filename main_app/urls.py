from django.urls import path, include
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
   path('foods/<int:pk>/delete_review/', views.ReviewDelete.as_view(), name='delete_reviews'),
   path('foods/<int:food_id>/add_photo/', views.add_photo, name='add_photo'),
   path('categories/create/', views.CategoryCreate.as_view(), name='category_create'),
   path('categories/<int:food_id>/assoc_category/<int:category_id>/', views.assoc_category, name='assoc_category'),
   path('categories/<int:food_id>/unassoc_category/<int:category_id>/', views.unassoc_category, name='unassoc_category'),
   path('accounts/', include('django.contrib.auth.urls')),
   path('accounts/signup', views.signup, name='signup')
]