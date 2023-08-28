from django.urls import path
from . import views
app_name='payments'
urlpatterns = [
    # path('<int:total_amount>/',views.order_payment,name='payment'),
    # path('paymenthandler/',views.paymenthandler,name='paymenthandler'),
]
