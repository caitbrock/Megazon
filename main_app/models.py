from unicodedata import category
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORY_TYPE = (
        ('D', 'Digital Art'),
        ('C', 'Course'),
        ('M', 'Music'),
        ('S', 'Service')
    )

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='userProfileImages')
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    category_type = models.CharField(max_length=1, choices=CATEGORY_TYPE, default=CATEGORY_TYPE[0][0])
    img = models.ImageField(upload_to='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quant_sell = models.IntegerField()
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quant_ordered = models.IntegerField()
    available = models.BooleanField(default=False)
    trading_price = models.IntegerField()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail', kwargs={'product_id': self.id})