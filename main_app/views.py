from django.shortcuts import redirect, render
from .models import Product,Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.urls import reverse
from .form import CustomUserCreationForm
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
   return redirect(reverse("dashboard"))

def cart(request):
    return render(request, 'cart.html')

def profile(request):
    user = Profile.objects.get(user=request.user)
    products = Product.objects.all()
    return render(request, 'profile.html',{'products': products,'user':user})

class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'description', 'price','img','quant_sell']
    success_url = '/'

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'description', 'price']

class ProductDelete(DeleteView):
    model = Product
    success_url = '/'

class ProfileCreate(CreateView):
    model = Profile
    fields = '__all__'
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)
    success_url = '/profile/'