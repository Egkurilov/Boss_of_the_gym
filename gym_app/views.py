from django.shortcuts import render
from django.http import HttpResponse

def gym_app(request):
    return HttpResponse("Hello, Django!")