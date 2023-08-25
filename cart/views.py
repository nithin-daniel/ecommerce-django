from django.shortcuts import render,redirect
from . models import CartItem
# from accounts.models import 
from django.conf import settings
from store.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F ,Sum
# Create your views here.
@login_required()
def cart_page(request):
    user = request.user
    total_amount = 0
    get_product = CartItem.objects.filter(user=user).annotate(total_amount=Sum(F('product__prize')*F('quantity')))
    total_amount = sum(item.total_amount for item in get_product)
    context = {
        'product' : get_product,
        'total_amount':total_amount
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

def delete_item(request,id):
    CartItem.objects.filter(product__product_id=id).delete()
    messages.success(request,'Product Deleted')
    return redirect('cart:cart')

def decrement_quantity(request,id):
    decrement = CartItem.objects.filter(product=id)
    for dec in decrement:
        if dec.quantity == 1:
            break
        dec.quantity = dec.quantity - 1
        dec.save()
        
    return redirect('cart:cart')

def increment_quantity(request,id):
   increment = CartItem.objects.filter(product=id)
   for inc in increment:
        inc.quantity = inc.quantity + 1
        inc.save()
   return redirect('cart:cart')