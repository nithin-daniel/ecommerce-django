from django.contrib import admin
from . models import CartItem,Order
# Register your models here.
admin.site.register(CartItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id','payment_method']
admin.site.register(Order,OrderAdmin)