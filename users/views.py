from catalog.models import Item

import django.contrib.auth.views as admin_views
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from users.forms import ProfileForm, UserForm, UserRegistrationForm
from users.models import CustomUser
from users.models import Profile


class SignUpView(View):
    template_name = 'users/signup.html'

    def get(self, request, form=None):
        context = {
            'form': form or UserRegistrationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
        return self.get(request, form)


class ProfileView(View):
    template_name = 'users/profile.html'

    def get(self, request, user_form=None, profile_form=None):
        liked_items = Item.objects.user_liked_items(request.user)

        context = {
            'items': liked_items,
            'user_form': user_form or UserForm(instance=request.user),
            'profile_form': profile_form or ProfileForm(instance=request.user.profile)
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_page')
        return self.get(request, UserForm, ProfileForm)


class UserDetailView(View):
    template_name = 'users/user_detail.html'

    def get(self, request, id_user):
        user = get_object_or_404(CustomUser.objects.only(
            'email', 'first_name', 'last_name', 'profile__birthday'
        ).select_related('profile'), pk=id_user)
        liked_items = Item.objects.user_liked_items(user)

        context = {
            'user': user,
            'items': liked_items,
        }
        return render(request, self.template_name, context=context)


class UserListView(View):
    template_name = 'users/user_list.html'

    def get(self, request):
        users = CustomUser.objects.all().prefetch_related(
            Prefetch('profile', queryset=Profile.objects.all())
        )

        context = {
            'users': users
        }
        return render(request, self.template_name, context=context)


class LoginView(admin_views.LoginView):
    template_name = 'users/login.html'


class PasswordChangeDoneView(admin_views.PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class LogoutView(admin_views.LogoutView):
    template_name = 'users/logout.html'


class PasswordResetView(admin_views.PasswordResetView):
    template_name = 'users/password_reset.html'


class PasswordResetDoneView(admin_views.PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class PasswordResetConfirmView(admin_views.PasswordResetConfirmView):
    template_name = 'users/reset.html'


class PasswordResetCompleteView(admin_views.PasswordResetCompleteView):
    template_name = 'users/reset_done.html'


class PasswordChangeView(admin_views.PasswordChangeView):
    template_name = 'users/password_change.html'
