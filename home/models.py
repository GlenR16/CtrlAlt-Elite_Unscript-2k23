from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField()
    quality = models.CharField(max_length=14,blank=True,null=True)
    ocr = models.CharField(max_length=1024,blank=True,null=True)
    def __str__(self):
        return self.file.name



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email Address",unique=True,max_length=127)
    name = models.CharField(max_length=255)
    files = models.ManyToManyField(UploadedFile,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

