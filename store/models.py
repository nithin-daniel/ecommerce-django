import uuid
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
from django.conf import settings
# Create your models here.
class Product(models.Model):
    product_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image/', default='media/no-image-default.png')

    
    def __str__(self):
        return self.product_name