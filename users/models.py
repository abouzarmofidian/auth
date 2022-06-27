from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

class Profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=255)
    city = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    address = models.TextField()
    age = models.DateField(null=True,blank=True)
    postalcode = models.CharField(max_length=10,null=True,blank=True)
    linkedin = models.CharField(max_length=200,null=True,blank=True)
    resume_link = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def first_name(self):
        return f"{self.user.first_name}"

    def last_name(self):
        return f"{self.user.last_name}"