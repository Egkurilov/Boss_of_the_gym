from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginForm, RegisterForm


class LoginView(View):
    def get(self, request):
        context = {'redirect': request.GET.get('next', '/catalog')}
        return render(request, 'autorization/login_page.html', context=context)

    def post(self, request):
        print(request.POST)
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return JsonResponse(
                {'result': 'success', 'message': 'Вы успешно авторизрованы', 'redirect': request.POST['redirect']})

        return JsonResponse({'result': 'error', 'message': form.custom_single_error})


class RegisterView(View):
    def get(self, request):

        if request.user.is_authenticated:
            return redirect('/catalog', permanent=True)

        context = {'title': 'Регистрация'}
        return render(request, 'autorization/registration.html', context=context)

    def post(self, request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = request.POST.get("email")
            user.set_password(request.POST.get('password1'))
            user.save()
            login(request, user)
            return JsonResponse(
                {'result': 'success', 'message': 'Вы успешно зарегистрированы'})

        print(form.errors)
        return JsonResponse({'result': 'error', 'message': form.custom_single_error})


class ForgetView(View):
    def get(self, request):
        return render(request, 'autorization/forget_password.html')
