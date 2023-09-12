import razorpay
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F ,Sum
from cart.models import CartItem
from accounts.models import CustomUser
def payment(request,total_amount):
    print(total_amount)
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    payment = client.order.create({'amount':int(total_amount) * 100,'currency':'INR','payment_capture':1})
    print(payment)
    return render(request,'checkout/success.html')

def checkout(request):
    user = request.user
    get_product = CartItem.objects.filter(user=user).annotate(total_amount=Sum(F('product__prize')*F('quantity')))
    total_amount = sum(item.total_amount for item in get_product)
    get_user_data = CustomUser.objects.filter(email=request.user.email).first()
    context = {
        'product' : get_product,
        'total_amount':total_amount,
        'current_user':get_user_data,
    }
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        address_1 = request.POST['Address1']
        address_2 = request.POST['Address2']
        payment_method = request.POST['paymentMethod']
        arr = []
        for product in get_product:
            prodct_name = product.product
            product_quantity = product.quantity
            arr.append((prodct_name,product_quantity))
        if not payment_method == 'COD':
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
            payment = client.order.create({'amount':int(total_amount) * 100,'currency':'INR','payment_capture':1})
            order_id = payment['id']
            order_status = payment['status']
            # if order_status == 'created':

    return render(request,'checkout/checkout.html',context)

@csrf_exempt
def success(request):
    if request.method == 'POST':
        value = request.POST
        print(value)
    return render(request,'checkout/success.html')

