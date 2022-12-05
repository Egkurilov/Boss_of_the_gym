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
                request.session['id'] = User.objects.values(id)
                return render(request, 'autorization/login_page.html', context={'error': 'Пользователя не существует'})
                 
        return redirect('/')


class RegisterView(View):
    def get(self, request):
        return render(request, 'autorization/registration.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            email = re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email)
            password = re.match(r'[а-яА-Яa-zA-Z0-9]*', password)
        if email.group(0) and password.group(0):
            if User.objects.values().filter(email=email.group(0)):
                return render(request, 'autorization/registration.html', context={'error': 'пользователь существует'})

            User.objects.create(password=password.group(0), email=email.group(0))
            
            user_id = User.objects.values('id').filter(email=email.group(0))
            request.session['id'] = user_id[0]['id']
        return render(request, 'autorization/login_page.html')

class ForgetView(View):
    def get(self, request):
        return render(request, 'autorization/forget_password.html')

