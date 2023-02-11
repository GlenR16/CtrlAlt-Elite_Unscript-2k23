from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager

# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=127)
    def __str__(self):
        return self.name

class Invoice(models.Model):
    date = models.DateField()
    amount = models.IntegerField()
    treatment = models.CharField(max_length=255)
    def __str__(self):
        return self.treatment

class Appointment(models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    doctor = models.CharField(max_length=255)
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    date = models.DateTimeField()
    def __str__(self) -> str:
        return self.doctor

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email Address",unique=True,max_length=127)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15,default=0)
    allergies = models.CharField(max_length=255,blank=True,null=True)
    weight = models.IntegerField(default=0)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE,blank=True,null=True)
    invoices = models.ManyToManyField(Invoice)
    appointments = models.ForeignKey(Appointment,on_delete=models.SET_NULL,null=True,blank=True)
    dob = models.DateField(blank=True,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name


