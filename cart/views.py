from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='accounts/login')
def add_to_cart(request):
    return render(request,'cart/cart.html')