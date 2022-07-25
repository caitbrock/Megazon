from unicodedata import category
from django.db import models
from django.urls import reverse

CATEGORY_TYPE = (
        ('D', 'Digital Art'),
        ('C', 'Course'),
        ('M', 'Music'),
        ('S', 'Service')
    )
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category_type = models.CharField(max_length=1, choices=CATEGORY_TYPE, default=CATEGORY_TYPE[0][0])
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    img = models.ImageField()
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
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