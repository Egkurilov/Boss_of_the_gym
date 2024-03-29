from django.contrib.auth.decorators import login_required
from django.urls import path

from account import views
from account.views import Image, ProfileView, SettingsView

urlpatterns = [
    path("profile", login_required(ProfileView.as_view()), name='profile'),
    path("settings", login_required(SettingsView.as_view())),
    path("settings/upload", login_required(Image.as_view())),
]
