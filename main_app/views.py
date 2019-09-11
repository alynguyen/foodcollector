from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Food, Review
from .forms import ReviewForm

# Create your views here.

class FoodCreate(CreateView):
  model = Food
  fields = '__all__'

class FoodDelete(DeleteView):
  model = Food
  success_url = '/foods/'

class FoodUpdate(UpdateView):
  model = Food
  fields = ['location', 'city', 'comments', 'rating']

def add_review(request, food_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.food_id = food_id
    new_review.save()
  return redirect('details', food_id=food_id)

def home(request):
  return HttpResponse('Home')

def about(request):
  return render(request, 'about.html')

def food_index(request):
  foods = Food.objects.all()
  return render(request, 'foods/index.html', {'foods': foods})

def food_details(request, food_id):
  food = Food.objects.get(id=food_id)
  review_form = ReviewForm()
  return render(request, 'foods/details.html', {'food': food, 'review_form': review_form})
  