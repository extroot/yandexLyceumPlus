from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from users.forms import UserLoginForm
from users.forms import UserRegistrationForm


def sighup(request):
    TEMPLATE_NAME = 'users/signup.html'

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('profile_page')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, TEMPLATE_NAME, context)


def login_page(request):
    TEMPLATE_NAME = 'users/login.html'

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('profile_page')
                    # return HttpResponse('Authenticated successfully')
                else:
                    form.add_error(None, 'Аккаунт не активен')
            else:
                form.add_error(None, 'Пользователь не найден')
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, TEMPLATE_NAME, context)


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
