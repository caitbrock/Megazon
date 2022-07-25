from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dashboard(request):
    return render(request, "users/dashboard.html")