from django.shortcuts import render
from store.models import Product
from cart.models import CartItem
# Create your views here.
def home(request):
    all_product = Product.objects.all()
    print(request.user)
    context = {
        'all_product':all_product
    }
    return render(request,'home.html',context)

def product_detail(request,id):
    all_product = Product.objects.filter(product_id=id)
    context = {
        'all_product':all_product
    }
    return render(request,'product-detail-page.html',context)

def total_count(request):
    total_count = CartItem.objects.filter(user=request.user).count()
    context = {
        'total_count':total_count
    }
    return render(request,'base.html',context)