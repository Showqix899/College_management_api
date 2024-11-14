#from django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

#from rest framework


#from app .manager
from .manager import CustomUserManager
# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    date_joined=models.DateTimeField(auto_now_add=True)

    objects=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]


    def __str__(self):
        return self.email