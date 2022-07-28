from urllib import request
from django.shortcuts import redirect, render
from .models import Product, Profile, Order
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.urls import reverse
from .form import CustomUserCreationForm, ProductForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.


# Create your views here.
# (when without filter) The home page will randomly grab products from the database
# 2022.07.23 for now the home will just show all products that we have --Roccay

def home(request):
    products = Product.objects.all()
    return render (request, 'home.html', {'products': products})

def products_detail(request,product_id):
  product = Product.objects.get(id=product_id)
  return render (request, 'products/detail.html', {
    'product': product,
  })
def about(request):
    return render(request, 'about.html')


def register(request):
 if request.method == "GET":
   return render(
    request, "registration/register.html",
    {'form': CustomUserCreationForm }
   )
 elif request.method == 'POST':
  form = CustomUserCreationForm(request.POST)
  if form.is_valid():
   user = form.save()
   login(request, user)
   return redirect(reverse("profile_create"))

def cart(request):

    return render(request, 'cart.html')

def profile(request):
    if(Profile.objects.get(user=request.user)):
        profile = Profile.objects.get(user=request.user)
        products = Product.objects.filter(user=request.user)
        return render(request, 'profile.html',{'products': products,'profile':profile})
    else:
        return redirect("profile_create")

class ProductCreate(CreateView):

    model = Product
    fields = ['name', 'description','category_type', 'price','img','quant_sell']
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
    # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)
    success_url = '/profile/'

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'description', 'price']
    success_url = '/profile/'

class ProductDelete(DeleteView):
    model = Product
    success_url = '/profile/'

class ProductDetailView(DetailView):
    model = Product

class ProductListView(ListView):
    model = Product

class ProfileCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name', 'email','description','img']
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
    # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)
    success_url = '/profile/'

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'email','description','img']
    success_url = '/profile/'



@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
 