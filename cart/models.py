from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
User= get_user_model()
# Create your models here.
class cart(models.Model):
    product_id = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.product_id