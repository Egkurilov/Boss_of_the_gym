from django.urls import path
from gym_app import views

urlpatterns = [
    path("", views.gym_app, name="gym_app"),
]