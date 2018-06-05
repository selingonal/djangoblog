from django.db import models
from datetime import date
import datetime

class User(models.Model):
    userName = models.CharField(max_length = 500)
    userAge = models.CharField(max_length= 3)
    dateJoined = models.CharField(max_length= 10)
    bio = models.CharField(max_length= 280)
    avi = models.CharField(max_length= 1000)

