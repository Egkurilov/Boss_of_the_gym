from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class StatisticView(View):
    def get(self, request):
        return render(request, 'statistic/statistic_page.html')
