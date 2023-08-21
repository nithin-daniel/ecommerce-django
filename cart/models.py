from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from store.models import Product
from datetime import datetime
# from django.contrib.auth.models import User
# from django.contrib.auth.models import User
# User= get_user_model()
from django.conf import settings
# Create your models here.
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return  self.product.product_name