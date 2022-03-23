from django.shortcuts import HttpResponse


def description(request):
    return HttpResponse('<h1>О проекте</h1>')
