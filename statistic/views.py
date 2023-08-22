from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class StatisticView(View):
    def get(self, request):
        # TODO заменить заглушку на модель, которую можно подгружать из профиля пользователя
        user_statistics_data = dict(
            monday = 100,
            tuesday = 200,
            wednesday = 300,
            thursday = 400,
            friday = 500,
            saturday = 650,
            sunday = 1000
        )

        weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

        for weekday in weekdays:
            user_statistics_data[weekday + "_percent"] = round(user_statistics_data.get(weekday) / 1000 * 100)

        return render(request, 'statistic/statistic_page.html', context={"user_statistics_data": user_statistics_data})
