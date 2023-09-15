import razorpay
from django.conf import settings
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F ,Sum
from cart.models import CartItem,Order
from accounts.models import CustomUser
from datetime import date
import uuid
from django.contrib import messages
from decouple import config
from django.contrib.auth.decorators import login_required
import json
@login_required()
def checkout(request):
    user = request.user
    get_product = CartItem.objects.filter(user=user).annotate(total_amount=Sum(F('product__prize')*F('quantity')))
    total_amount = sum(item.total_amount for item in get_product)
    get_user_data = CustomUser.objects.filter(email=request.user.email).first()
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    razorpay_order = client.order.create({'amount':int(total_amount) * 100,'currency':'INR','payment_capture':1})
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/payment/callback'
    context = {
        'product' : get_product,
        'total_amount':total_amount,
        'current_user':get_user_data,
        'razorpay_order_id':razorpay_order_id,
        'callback_url':callback_url,
        'currency':'INR',
        'razorpay_merchant_key':settings.RAZORPAY_KEY_ID,
        'user_name':request.user.first_name
    }
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        address_1 = request.POST['Address1']
        payment_method = request.POST['paymentMethod']
        arr = []
        for product in get_product:
            prodct_name = product.product
            product_quantity = product.quantity
            arr.append((prodct_name,product_quantity))
        if not payment_method == 'COD':
            RAZORPAY_KEY_ID = config('RAZOR_KEY_ID')
            RAZORPAY_KEY_SECRET = config('RAZOR_KEY_SECRET')
            client = razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET))
            payment = client.order.create({'amount':int(total_amount) * 100,'currency':'INR','payment_capture':1})
            order_id = payment['id']
            amount = payment['amount']
            order_status = payment['status']
            callback_url = 'http://127.0.0.1:8000/'+'payment/callback/'
            context = {
                'key':RAZORPAY_KEY_ID,
                'order_id':order_id,
                'amount':amount,
                'callback_url':callback_url
            }
            order_insert = Order(order_id=order_id,customer_id=request.user,date_of_order=date.today(),shipping_address=address_1,payment_method=payment_method,order_total=total_amount,ordered_item=arr,user=request.user)
            order_insert.save()
            return render(request,'checkout/razorpay.html',context)
        else:
            order_insert = Order(order_id=uuid.uuid4(),customer_id=request.user,date_of_order=date.today(),shipping_address=address_1,payment_method=payment_method,order_total=total_amount,ordered_item=arr,user=request.user)
            order_insert.save()
            CartItem.objects.all().delete()
    
    return render(request,'checkout/checkout.html',context)

@csrf_exempt
def razorpay_callback(request):
    RAZORPAY_KEY_ID = config('RAZOR_KEY_ID')
    RAZORPAY_KEY_SECRET = config('RAZOR_KEY_SECRET')
    razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET))
    # only accept POST request.
    if request.method == "POST":
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            order_check = Order.objects.filter(order_id=razorpay_order_id)
            if order_check:
                 messages.success(request,'Payment Successfull')
                 CartItem.objects.filter(user=order_check.user).all().delete()
                 return redirect('home')
            else:
                messages.error(request,'Payment Failed Try Again')
                return redirect('payments:checkout')