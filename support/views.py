from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class SupportView(View):
    def get(self, request):
        return render(request, 'support/support_main_page.html')
