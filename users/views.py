from django.shortcuts import HttpResponse


def signup(request):
    return HttpResponse('<h1>Регистрация</h1>')


def profile(request):
    return HttpResponse('<h1>Мой профиль</h1>')


def user_detail(request, id_user):
    return HttpResponse('<h1>Информация о пользователе</h1>')


def user_list(request):
    return HttpResponse('<h1>Список пользователей</h1>')
