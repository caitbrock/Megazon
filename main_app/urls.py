from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),

#   path('cats/', views.cats_index, name='index'),
#   path('cats/<int:cat_id>/',views.cats_detail,name='detail')
  path('accounts/', include("django.contrib.auth.urls")),
  path('register/', views.register, name ="register"),
  path('products/<int:product_id>/', views.products_detail, name='detail'),
  path('profile/<int:profile_id>', views.profile, name='profile'),
  path('products/create/', views.ProductCreate.as_view(), name='products_create'),
  path('orders/<int:pk>/update', views.OrderUpdate.as_view(), name='orders_update'),
  path('products/<int:pk>/update', views.ProductUpdate.as_view(), name='products_update'),
  path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='products_delete'),
  path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
  path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name='profile_update'),
path('cart/', views.cart, name='cart'),
  path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
  path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
  path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
  path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
  path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
  path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
  path('checkout/',views.checkout,name='checkout'),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
