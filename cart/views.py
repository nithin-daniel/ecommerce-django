from django.shortcuts import render,redirect
from . models import CartItem
# from accounts.models import 
from django.conf import settings
from store.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def cart_page(request):
    user = request.user
    get_product = CartItem.objects.all().delete()
    print(get_product)
    return render(request,'cart/cart.html')

@login_required()
def add_to_cart(request,id):
    # product = Product.objects.get(product_id=id)
    user = request.user
    # if not Cart.objects.filter(user=user).exists():
    #     Cart.objects.create(user=user)
    #     if not CartItem.objects.filter(product=product).exists():
    #         CartItem.objects.create(product=product)
    #         return redirect('home')
    #     else:
    #         messages.warning(request,"Product already added")
    #         return redirect('home')
    # else:
    #     messages.warning(request,"Product added Successfully")
    cart_item = CartItem.objects.filter(user=user,product__product_id=id)
    if cart_item.exists():
        item = cart_item.first()
        item.quantity += 1
        item.save()
    else:
        prod = Product.objects.get(product_id=id)
        CartItem.objects.create(user=user,product=prod)
    return redirect('home')