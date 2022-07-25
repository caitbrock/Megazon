from django.urls import path, include
from . import views  


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
#   path('cats/', views.cats_index, name='index'),
#   path('cats/<int:cat_id>/',views.cats_detail,name='detail')
  path('dashboard/', views.dashboard, name="dashboard"),
  path('accounts/', include("django.contrib.auth.urls"))
]