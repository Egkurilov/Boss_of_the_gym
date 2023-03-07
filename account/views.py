from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import User
from django.http import JsonResponse
import base64
import logging

logger = logging.getLogger(__name__)


def profile(request):
    return HttpResponse("Hello, Django!")


class ProfileView(View):
    def get(self, request):
        user_data = User.objects.values().filter(id=request.user.id).first()

        return render(request, 'user/profile.html', context={'user_data': user_data})


class Image(View):
    def post(self, request):
        # TODO сделать ресайз картинки
        # TODO проверка что это картинка
        avatar = request.FILES['avatar'].read()
        User.objects.values().filter(id=request.user.id).update(avatar=base64.b64encode(avatar).decode('utf-8'))
        logger.info("user uploadded new avatar")
        return JsonResponse({'result': "success", 'message': 'OK'})


class SettingsView(View):
    def get(self, request):
        user_data = User.objects.values().filter(id=request.user.id).first()
        return render(request, 'user/settings.html', context={'user_data': user_data})

    def post(self, request):
        try:
            name = request.POST.get('name')
            age = request.POST.get('age')
            weight = request.POST.get('weight')

            if not str(age).isnumeric():
                raise Exception('Введите возраст в корректном формате')
            age = int(age)
            if age < 10 or age > 80:
                raise Exception('Введите возраст в корректном формате')

            if not str(weight).isnumeric():
                raise Exception('Введите вес в корректном формате')
            weight = int(weight)
            if weight < 10 or weight > 150:
                raise Exception('Введите вес в корректном формате')

            User.objects.values().filter(id=request.user.id).update(first_name=name, datebirth=15, weight=weight)
            logger.info("GET USER DATA PROFILE")
        except Exception as error:
            return JsonResponse({'result': "error", 'message': str(error)})

        return JsonResponse({'result': "success", 'message': 'OK'})
