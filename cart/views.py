from django.shortcuts import render,redirect
from . models import CartItem
# from accounts.models import 
from django.conf import settings
from store.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def cart_page(request):
    user = request.user
    get_product = CartItem.objects.filter(user=user)
    for product in get_product:
        img = product.product.image   
    context = {
        'product' : get_product
    }
    return render(request,'cart/cart.html',context)

@login_required()
def add_to_cart(request,id):
    user = request.user
    cart_item = CartItem.objects.filter(user=user,product__product_id=id)
    if cart_item.exists():
        item = cart_item.first()
        item.quantity += 1
        item.save()
    else:
        prod = Product.objects.get(product_id=id)
        CartItem.objects.create(user=user,product=prod)
        messages.info(request,'Product Added')
    return redirect('home')

def delete_item(request):
    return redirect('cart')