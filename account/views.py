from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def profile(request):
    return HttpResponse("Hello, Django!")


class ProfileView(View):
    def get(self, request):
        return render(request, 'user/profile.html')

class SettingsView(View):
    def get(self, request):
        return render(request, 'user/settings.html')
