from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class StatisticView(View):
    def get(self, request):
        # TODO Сделать модель, которую можно подгружать из профиля пользователя и заполнение прогресс бара
        # Сделать подстройку прогресс бара под значения дней недели
        # Подстройку прогресс бара можно сделать через математический фильтр в шаблоне страницы
        user_statistics_data = dict(
            monday = 100,
            tuesday = 200,
            wednesday = 300,
            thursday = 400,
            friday = 500,
            saturday = 600,
            sunday = 1000
        )

        return render(request, 'statistic/statistic_page.html', context={"user_statistics_data": user_statistics_data})
