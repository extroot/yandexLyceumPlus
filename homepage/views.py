from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('<h1>Главная</h1>')
