from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from autorization.models import User

class MyError(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
 
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))



def profile(request):
    return HttpResponse("Hello, Django!")


class ProfileView(View):
    def get(self, request):
        return render(request, 'user/profile.html')

class SettingsView(View):
    def get(self, request):
        return render(request, 'user/settings.html')

    def post(self, request):
        try:
            name = request.POST.get('name')
            age = request.POST.get('age')
            weight = request.POST.get('weight')
        except MyError as error:
            print('A New Exception occurred: ', error.value)
            return render(request, 'user/settings.html') 

        User.objects.values().filter(id=request.session['id']).update(user_name=name, age=age, weight=weight)


        return render(request, 'user/settings.html')
