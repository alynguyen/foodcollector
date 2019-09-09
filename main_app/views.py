from django.shortcuts import render
from django.http import HttpResponse
from .models import Food

# Create your views here.

def home(request):
  return HttpResponse('Home')

def about(request):
  return render(request, 'about.html')

def food_index(request):
  foods = Food.objects.all()
  return render(request, 'foods/index.html', {'foods': foods})

def food_details(request, food_id):
  food = Food.objects.get(id=food_id)
  return render(request, 'foods/details.html', {'food': food})
  