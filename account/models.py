from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    gender = models.CharField(max_length=500, blank=True)
    weight = models.CharField(max_length=30, blank=True)
    datebirth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(default='', blank=True)
