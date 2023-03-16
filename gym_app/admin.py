from django.contrib import admin

# Register your models here.
from account.models import User
from exercises.models import ExerciseList


class UserList(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "last_login")
    list_filter = ("id", "username")


class Exercises(admin.ModelAdmin):
    list_display = ("id", "name", "cost")
    list_filter = ("id", "name")


admin.site.register(User, UserList)
admin.site.register(ExerciseList, Exercises)
