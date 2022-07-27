from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm

from main_app.models import Product

class CustomUserCreationForm(UserCreationForm):
 class Meta(UserCreationForm.Meta):
    fields = UserCreationForm.Meta.fields + ("email",)
         
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['type']
