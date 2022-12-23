from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Permission
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.utils import timezone
User = settings.AUTH_USER_MODEL
from django.core.exceptions import ValidationError


class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password,**extra_fields):
        if not username:
            raise valueError("User must have username!")
        if not email:
            raise valueError("User must have email!")
        user = self.model(email=self.normalize_email(email),username=username,
							password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password, **extra_fields):
        user = self.create_user(email=self.normalize_email(email), username=username, password=password, 
							**extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class UserProfile(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, null=True, blank=True)
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = MyAccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def __str__(self):
        try:
            return str(self.email)
        except:
            return "_"
        
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class Movies(models.Model):
    cast=models.ManyToManyField('Cast',blank=True)
    title=models.CharField(max_length=200, null=True, blank=True)
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now_add=True)
    runtime=models.IntegerField(default=0.00)
    language= models.CharField(max_length=200, null=True, blank=True)
    tagline=models.CharField(max_length=200, null=True, blank=True)

    

class Cast(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    dob= models.DateField()
    gender= models.CharField(max_length=200, null=True, blank=True)
    
    
    
    
    
    
    
    
    
    
    
    
    