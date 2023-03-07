from django.contrib.auth.views import LogoutView
from django.urls import path
from autorization.views import LoginView
from autorization.views import RegisterView
from autorization.views import ForgetView


urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('forget', ForgetView.as_view()),
    path('logout', LogoutView.as_view(), name='account_logout'),
]