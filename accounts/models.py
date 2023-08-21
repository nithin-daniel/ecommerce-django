from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password,username,phone_number, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,last_name=last_name,username=username,phone_number=phone_number,**other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,first_name,last_name,password,username=None,phone_number=None, **other_fields):

        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email,first_name,last_name,password,username,phone_number,**other_fields)

    
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('Email Address'),unique=True)
    password = models.CharField(_('Password Field'),max_length = 25)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True,default=None,blank=False,null=True)
    phone_number = models.CharField(max_length=50,default=None,blank=False,null=True)


    # requried
    date_joined = models.DateTimeField(auto_now_add = True)
    last_joined = models.DateTimeField(default=timezone.now,editable=False, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomAccountManager()


    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return str(self.email)