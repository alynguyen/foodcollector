from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
import uuid
import boto3
from .models import Food, Review, Photo, Category
from .forms import ReviewForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'foodcollect'

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

class CategoryCreate(CreateView):
  model = Category
  fields = '__all__'

def add_photo(request, food_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, food_id=food_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('details', food_id=food_id)

def add_review(request, food_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.food_id = food_id
    new_review.save()
  return redirect('details', food_id=food_id)

def delete_review(request, review_id, food_id):
  Review.objects.get(id=review_id)
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
  