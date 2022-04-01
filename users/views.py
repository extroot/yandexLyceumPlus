from django.shortcuts import render


def signup(request):
    context = {}
    return render(request, 'users/signup.html', context=context)


def profile(request):
    context = {}
    return render(request, 'users/profile.html', context=context)


def user_detail(request, id_user):
    context = {"id_user": id_user}
    return render(request, 'users/user_detail.html', context=context)


def user_list(request):
    context = {}
    return render(request, 'users/user_list.html', context=context)
