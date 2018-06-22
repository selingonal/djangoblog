from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_blogger = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
