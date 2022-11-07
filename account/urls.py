from django.urls import path
from account import views
from account.views import ProfileView, SettingsView


urlpatterns = [
    path("profile", ProfileView.as_view()),
    path("settings", SettingsView.as_view()),
]