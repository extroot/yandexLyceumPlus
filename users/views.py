from catalog.models import Item

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, redirect, render

from users.forms import ProfileForm, UserForm, UserLoginForm, UserRegistrationForm
from users.models import Profile


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
                else:
                    form.add_error(None, 'Аккаунт не активен')
            else:
                form.add_error(None, 'Пользователь не найден')
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, TEMPLATE_NAME, context)


def logout_page(request):
    # TODO: message when user is not authenticated
    logout(request)
    return redirect('homepage')


def profile(request):
    liked_items = Item.objects.user_liked_items(request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_page')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'items': liked_items,
        'user_form': user_form,
        'profile_form': profile_form
    }
    TEMPLATE_NAME = 'users/profile.html'
    return render(request, TEMPLATE_NAME, context=context)


def user_detail(request, id_user):
    user = get_object_or_404(User.objects.only(
        'email', 'first_name', 'last_name', 'profile__birthday'
    ).select_related('profile'), pk=id_user)
    liked_items = Item.objects.user_liked_items(user)

    context = {
        'user': user,
        'items': liked_items,
    }

    TEMPLATE_NAME = 'users/user_detail.html'
    return render(request, TEMPLATE_NAME, context=context)


def user_list(request):
    users = User.objects.all().prefetch_related(
        Prefetch('profile', queryset=Profile.objects.all())
    )

    context = {
        'users': users
    }

    TEMPLATE_NAME = 'users/user_list.html'
    return render(request, TEMPLATE_NAME, context=context)
