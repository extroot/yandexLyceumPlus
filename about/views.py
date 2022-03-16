from django.shortcuts import HttpResponse


def description(request):
    return HttpResponse('<h1>Главная</h1>')
