from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
     email = models.EmailField(unique=True)
     phone_number = PhoneNumberField(unique=True, blank=True, null=True)
     location = models.CharField(max_length=255, blank=True, null=True)
     language_preference = models.CharField(
          max_length=255, 
          blank=True, 
          null=True, 
          choices = [
               ('en', 'English'),
               ('yo', 'Yoruba'),
               ('ig', 'Igbo'),
               ('ha', 'Hausa'),
               ('fr', 'French'),
          ], 
          default='en'
     )
     def __str__(self):                               
          return self.username
