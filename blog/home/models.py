from django.db import models

class Home(models.Model):
    icon = models.CharField(max_length= 1000)