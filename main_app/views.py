from django.shortcuts import redirect, render
from .models import Product, Profile, Order
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.urls import reverse
from .form import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.


# Create your views here.
# (when without filter) The home page will randomly grab products from the database
# 2022.07.23 for now the home will just show all products that we have --Roccay

def home(request):
    products = Product.objects.all()
    try:
        currentUser = Profile.objects.get(user=request.user)
        return render (request, 'home.html', {'products': products,'currentUser':currentUser})
    except:
        return render (request, 'home.html', {'products': products})

def products_detail(request,product_id):
  product = Product.objects.get(id=product_id)
  currentUser = request.user
  return render (request, 'products/detail.html', {
    'product': product,
    'currentUser':currentUser
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

def profile(request,profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
        products = Product.objects.filter(user=profile.user)
        orders=Order.objects.filter(user=profile.user)
        currentUser = request.user
        return render(request, 'profile.html',{'products': products,'profile':profile,'collections':orders,'currentUser':currentUser})
    except:
        profile = Profile.objects.get(id=profile_id)
        products = Product.objects.filter(user=profile.user)
        orders=Order.objects.filter(user=profile.user)
        return render(request, 'profile.html',{'products': products,'profile':profile,'collections':orders})

def profileRedirect(request):
    profile = Profile.objects.get(user=request.user)
    products = Product.objects.filter(user=request.user)
    orders=Order.objects.filter(user=request.user)
    return render(request, 'profile.html',{'products': products,'profile':profile,'collections':orders})


class ProductCreate(CreateView):

    model = Product
    fields = ['name', 'description', 'price','category_type','img','quant_sell']

    def get_success_url(self):
        id = self.request.user.profile.id
        return f'/profile/{id}'

class OrderUpdate(UpdateView):

    model = Order
    fields = ['available', 'trading_price']

    def get_success_url(self):
        id = self.request.user.profile.id
        return f'/profile/{id}'


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'description', 'price']
    
    def get_success_url(self):
        id = self.request.user.profile.id
        return f'/profile/{id}'

    

class ProductDelete(DeleteView):
    model = Product
    def get_success_url(self):
        id = self.request.user.profile.id
        return f'/profile/{id}'

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

    def get_success_url(self):
        id = self.request.user.profile.id
        return f'/profile/{id}'

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'email','description','img']
    def get_success_url(self):
        id = self.request.user.profile.id
        return f'/profile/{id}'

def checkout(request):
    for item in Cart(request).__dict__['cart'].items():

        order=Order.objects.create(
            product=Product.objects.get(id=item[1]['product_id']),
            quant_ordered = item[1]['quantity'],
            available = False,
            trading_price = 0,
            user=request.user
        )
        Order.save(order)
    cart_clear(request)
    return redirect("home")


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