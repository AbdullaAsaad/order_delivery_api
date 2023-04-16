from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password,**other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError('super user must be assigned to is_staff=True')
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError('super user must be assigned to is_superuser=True')
        
        return self.create_user(email, user_name, first_name, password,**other_fields)
    
    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('email must be provided'))
        
        email = self.normalize_email(email)
        user = self.model(user_name=user_name, email=email, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
class NewUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(verbose_name="Email", unique=True, max_length=60)
    user_name = models.CharField(max_length=40,unique=True)
    first_name = models.CharField(max_length=30,blank=True)
    start_date = models.DateField(default=timezone.now)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'user_name']
    
    def __str__(self):
        return self.user_name