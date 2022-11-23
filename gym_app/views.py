from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class CatalogView(View):
    def get(self, request):
        return render(request, 'gym_app/main_page.html')

class AddView(View):
    def get(self, request):
        return render(request, 'gym_app/add_execises.html')