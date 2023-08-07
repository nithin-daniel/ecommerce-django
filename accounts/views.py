from django.shortcuts import render,redirect
# from . models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
User = get_user_model()
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
        elif User.objects.filter(email=email):
            messages.info(request,'Email already used')
                         
        elif User.objects.filter(username=username):
            messages.info(request,'Username already used')
        else:
            user = User.objects.create_user(email=email,password=password2,username=username,phone_number=phone_number,first_name=first_name,last_name=last_name)
            user.is_active = True
            user.save()
            messages.success(request,'User Created Successfully')
            return redirect(user_login)
    return  render(request,'accounts/signup.html')

def user_login(request):
    if request.method == 'POST':
     
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,"Wrong Password")
        else:
            messages.error(request,"User Not Found")
        return render(request,'accounts/login.html')
    return render(request,'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')