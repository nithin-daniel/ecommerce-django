from django.shortcuts import render,redirect
from . models import CustomUser
from django.contrib import messages
# from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth import get_user_model

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
            user.is_active = True
            user.save()
            messages.success(request,'User Created Successfully')
            return redirect(login)
    return  render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request,"User Not Found")
        return render(request,'accounts/login.html')
    return render(request,'accounts/login.html')

# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth import get_user_model

# class EmailBackend(BaseBackend):
#     model = get_user_model()
#     def authenticate(
#         self, request = None, email=None, password=None):
#         try:
#             user = self.model.objects.get(email=email)
#         except self.model.DoesNotExist:
#             return None
#         if self.model.check_password(password) and user is not None:
#             return user

#     def get_user(self, user_id):
#         try:
#             return self.model.objects.get(pk=user_id)
#         except self.model.DoesNotExist:
#             return None