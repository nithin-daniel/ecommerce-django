from django.db import models

# Create your models here.
class cart(models.Model):
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cart_image/', default='media/no-image-default.png')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product_name