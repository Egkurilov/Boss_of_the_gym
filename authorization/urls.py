from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path
from authorization.views import LoginView
from authorization.views import RegisterView
from authorization.views import ForgetView


urlpatterns = [
    path('login', LoginView.as_view(), name='account_login'),
    path('register', RegisterView.as_view(), name='account_register'),
    path('forget', ForgetView.as_view(), name='account_forget'),
    path('logout', LogoutView.as_view(), name='account_logout'),
]