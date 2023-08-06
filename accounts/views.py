from django.shortcuts import render,redirect
from . models import CustomUser
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        username = request.POST['username']
        if not password1 == password2:
            messages.error(request,'Password not Matching!')
            return redirect(register)
        elif CustomUser.objects.filter(email=email):
            messages.info(request,'Email already used')
                         
        elif CustomUser.objects.filter(username=username):
            messages.info(request,'Username already used')
        else:
            user = CustomUser.objects.create_user(email=email,password=password2,username=username,phone_number=phone_number,first_name=first_name,last_name=last_name)
            user.save()
            messages.success(request,'User Created Successfully')
            return redirect(login)
    return  render(request,'accounts/signup.html')

def login(request):
    return render(request,'accounts/login.html')