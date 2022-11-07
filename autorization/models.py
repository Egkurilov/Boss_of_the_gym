from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=255, default=None)
    password = models.CharField(max_length=255, default=None)
    email = models.EmailField(max_length=255, default=None)
    date_joined = models.CharField(max_length=255, default=None)
    last_activity = models.CharField(max_length=255, default=None)
    age = models.IntegerField(default=None)
    weight = models.IntegerField(default=None)
    avatar = models.ImageField(default=None)

 