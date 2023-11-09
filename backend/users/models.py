from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    favorite_genre = models.CharField(max_length=50, blank=True, choices=[('terror', 'Terror')])
