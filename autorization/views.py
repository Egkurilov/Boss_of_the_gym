from django.shortcuts import render, redirect
from django.views import View
from .models import User
import re

class LoginView(View):
    def get(self, request):
        return render(request, 'autorization/login_page.html')

    def post(self, request):
        login = request.POST.get('email')
        password = request.POST.get('password')

        if login and password:
            login = re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', login)
            password = re.match(r'[а-яА-Яa-zA-Z0-9]*', password)
        if login.group(0) and password.group(0):
            if not User.objects.values().filter(email=login.group(0)):
                 return render(request, 'autorization/login_page.html', context={'error': 'Пользователя не существует'})

        return redirect('/')


class RegisterView(View):
    def get(self, request):
        return render(request, 'autorization/registration.html')

    def post(self, request):

        login = request.POST.get('login')
        password = request.POST.get('password')
        if login and password:
            login = re.match(r'[а-яА-Яa-zA-Z0-9]*', login)
            password = re.match(r'[а-яА-Яa-zA-Z0-9]*', password)
        if login.group(0) and password.group(0):
            if User.objects.values().filter(user_name=login.group(0)):
                return render(request, 'autorization/registration.html', context={'error': 'пользователь существует'})

            User.objects.create(user_name=login.group(0), password=password.group(0), last_activity="1", 
                                email=login.group(0), date_joined="1", age="10", weight="11", avatar="1")
            request.session['login'] = login.group(0)
            return redirect('/')

        return render(request, 'auth/registration.html')

class ForgetView(View):
    def get(self, request):
        return render(request, 'autorization/forget_password.html')

