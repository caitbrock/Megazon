from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, ProductFilter
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

# (when without filter) The home page will randomly grab products from the database
# 2022.07.23 for now the home will just show all products that we have --Roccay
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products': products})

def products_detail(request,product_id):
  product = Product.objects.get(id=product_id)
  return render(request,'products/detail.html', {
    'product': product,
  })

def about(request):
    return render(request, 'about.html')


def dashboard(request):
    return render(request, "users/dashboard.html")

def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'my_app/template.html', {'filter': f})

class ProductCreate(CreateView):
  model = Product
  fields = ['name','description','price']
  success_url = '/'


def cart(request):
    return render(request, 'cart.html')

def profile(request):
    return render(request, 'profile.html')

class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'img', 'quant_sell']

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'description', 'price']

class ProductDelete(DeleteView):
    model = Product
    success_url = '/'

