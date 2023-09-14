from django.urls import path
from . import views
app_name='payments'
urlpatterns = [
    path('checkout/',views.checkout,name='checkout'),
    path('callback/',views.razorpay_callback,name='razorpay_callback'),
]
