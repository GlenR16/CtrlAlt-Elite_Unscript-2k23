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
        
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email Address",unique=True,max_length=127)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    allergies = models.CharField(max_length=255)
    weight = models.IntegerField()
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    invoices = models.ManyToManyField(Invoices)
    appointments = models.ForeignKey()
    dob = models.DateField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

class Invoices(models.Model):
    date = models.DateField()
    amount = models.IntegerField()
    treatment = models.CharField(max_length=255)
    def __str__(self):
        return self.treatment

class appointments(models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    doctor = models.CharField(max_length=255)
    invoice = models.ForeignKey(Invoices,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.date
