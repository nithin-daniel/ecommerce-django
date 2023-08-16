from django.urls import path
from  . import views
app_name='cart'
urlpatterns = [
    path('',views.cart_page,name='cart'),
    path('add/<uuid:id>/',views.add_to_cart,name='cart-add'),
]
