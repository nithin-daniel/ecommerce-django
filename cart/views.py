from django.shortcuts import render,redirect
from . models import cart
from store.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def cart_page(request):
    return render(request,'cart/cart.html')

@login_required()
def add_to_cart(request,id):
    if cart.objects.filter(product_id=id).exists():
        messages.warning(request,'Product already added')
        return redirect('home')
    else:
        cart.objects.create(product_id=id)
        messages.success(request,'Product added successfully')
        return redirect('home')