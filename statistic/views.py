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
            saturday = 700,
            sunday = 1000
        )

        user_statistics_data["monday_percent"] = user_statistics_data.get('monday') / 1000 * 100
        user_statistics_data["tuesday_percent"] = user_statistics_data.get('tuesday') / 1000 * 100
        user_statistics_data["wednesday_percent"] = user_statistics_data.get('wednesday') / 1000 * 100
        user_statistics_data["thursday_percent"] = user_statistics_data.get('thursday') / 1000 * 100
        user_statistics_data["friday_percent"] = user_statistics_data.get('friday') / 1000 * 100
        user_statistics_data["saturday_percent"] = user_statistics_data.get('saturday') / 1000 * 100
        user_statistics_data["sunday_percent"] = user_statistics_data.get('sunday') / 1000 * 100
        

        return render(request, 'statistic/statistic_page.html', context={"user_statistics_data": user_statistics_data})
