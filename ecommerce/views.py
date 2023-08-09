from django.shortcuts import render
from store.models import Product
# Create your views here.
def home(request):
    all_product = Product.objects.all()
    context = {
        'all_product':all_product
    }
    return render(request,'home.html',context)