from django.shortcuts import render


def signup(request):
    context = {}
    TEMPLATE_NAME = 'users/signup.html'
    return render(request, TEMPLATE_NAME, context=context)


def profile(request):
    context = {}
    TEMPLATE_NAME = 'users/profile.html'
    return render(request, TEMPLATE_NAME, context=context)


def user_detail(request, id_user):
    context = {'id_user': id_user}
    TEMPLATE_NAME = 'users/user_detail.html'
    return render(request, TEMPLATE_NAME, context=context)


def user_list(request):
    context = {}
    TEMPLATE_NAME = 'users/user_list.html'
    return render(request, TEMPLATE_NAME, context=context)
