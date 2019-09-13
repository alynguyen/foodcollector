from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Food, Review, Photo, Category
from .forms import ReviewForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'foodcollect'

# Create your views here.

class FoodCreate(LoginRequiredMixin, CreateView):
  model = Food
  fields = ['name', 'location', 'city', 'comments', 'rating']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FoodDelete(LoginRequiredMixin, DeleteView):
  model = Food
  success_url = '/foods/'

class FoodUpdate(LoginRequiredMixin, UpdateView):
  model = Food
  fields = ['location', 'city', 'comments', 'rating']

class CategoryCreate(LoginRequiredMixin, CreateView):
  model = Category
  fields = '__all__'

class ReviewDelete(LoginRequiredMixin, DeleteView):
  model = Review
  def get_success_url(self):
        return reverse_lazy('details', kwargs={'food_id': self.object.food_id})

@login_required
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def assoc_category(request, food_id, category_id):
  Food.objects.get(id=food_id).categories.add(category_id)
  return redirect('details', food_id=food_id)

def unassoc_category(rquest, food_id, category_id):
  Food.objects.get(id=food_id).categories.remove(category_id)
  return redirect('details', food_id=food_id)

@login_required
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

@login_required
def add_review(request, food_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.food_id = food_id
    new_review.user = request.user.username
    new_review.save()
  return redirect('details', food_id=food_id)

@login_required
def delete_review(request, food_id):
  review = Review.objects.get(id=review_id)
  review.remove()
  return redirect('details', food_id=food_id)

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def food_index(request):
  foods = Food.objects.all()
  return render(request, 'foods/index.html', {'foods': foods})

@login_required
def food_details(request, food_id):
  food = Food.objects.get(id=food_id)
  categories_dont = Category.objects.exclude(id__in = food.categories.all().values_list('id'))
  review_form = ReviewForm()
  return render(request, 'foods/details.html', {
    'food': food, 
    'review_form': review_form,
    'categories': categories_dont,
    })
