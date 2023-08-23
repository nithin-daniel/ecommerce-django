from django.urls import path
from  . import views
app_name='cart'
urlpatterns = [
    path('',views.cart_page,name='cart'),
    path('add/<uuid:id>/',views.add_to_cart,name='cart-add'),
    path('delete/<uuid:id>/',views.delete_item,name='cart-delete'),
    path('minus/<uuid:id>/',views.decrement_quantity,name='cart-minus'),
]
