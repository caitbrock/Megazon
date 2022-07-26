from django.urls import path, include
from . import views  
from django.conf import settings  
from django.conf.urls.static import static 

urlpatterns = [
  path('', views.home, name='home'),
  path('', views.product_list, name="product-list"),
  path('about/', views.about, name='about'),
  path('dashboard/', views.dashboard, name="dashboard"),
  path('accounts/', include("django.contrib.auth.urls")),
  path('products/<int:product_id>/', views.products_detail, name='detail'),
  path('cart/', views.cart, name='cart'),
  path('profile/', views.profile, name='profile'),
  path('products/create/', views.ProductCreate.as_view(), name='products_create'),
  path('products/<int:pk>/update', views.ProductUpdate.as_view(), name='products_update'),
  path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='products_delete')

]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  