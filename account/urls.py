from django.urls import path
from account import views
from account.views import ProfileView, SettingsView, Image

urlpatterns = [
    path("profile", ProfileView.as_view()),
    path("settings", SettingsView.as_view()),
    path("settings/upload", Image.as_view()),
]
