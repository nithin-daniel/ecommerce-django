from cart.models import CartItem

def total_count(request):
    total_count = CartItem.objects.filter(user=request.user.id).count()
    return {'total_count':total_count}