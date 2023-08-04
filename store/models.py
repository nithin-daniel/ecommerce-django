import uuid
from django.db import models
# from django.contrib.auth import User
# Create your models here.
class Product(models.Model):
    product_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=True)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    # user = models.ForeignKey(User,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.product_name