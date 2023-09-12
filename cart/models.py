from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from store.models import Product
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return  self.product.product_name
    
class Order(models.Model):
    order_id = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    date_of_order = models.CharField(max_length=10)
    shipping_address = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=10)
    order_total = models.PositiveIntegerField()
    ordered_item = models.CharField(max_length=1000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.order_id
    