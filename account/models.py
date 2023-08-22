from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    gender = models.CharField(max_length=500, blank=True)
    weight = models.CharField(max_length=30, default=None, null=True, blank=True)
    datebirth = models.CharField(max_length=30, default=None, null=True, blank=True)
    avatar = models.ImageField(default=None, null=True, blank=True)
