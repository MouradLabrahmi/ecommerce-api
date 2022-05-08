from django.db import models

from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]

    username=models.CharField(max_length=40,unique=True)
    email=models.CharField(max_length=40,unique=True)
    phone_number=PhoneNumberField(unique=True,null=False,blank=False)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)

    REQUIRED_FIELDS=['username','phone_number']
    USERNAME_FIELD='email'

    def __str__(self):
        return f"User {self.username}"