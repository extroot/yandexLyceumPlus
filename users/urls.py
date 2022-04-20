import django.contrib.auth.views as admin_views
from django.urls import path

from users import views

urlpatterns = [
    path('signup/', views.sighup, name='signup'),
    # path('login/', views.login_page, name='login'),
    # path('logout/', views.logout_page, name='logout'),

    path('profile/', views.profile, name='profile_page'),
    path('users/<int:id_user>/', views.user_detail, name='user_page'),
    path('users/', views.user_list, name='all_users'),

    path('login/', admin_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', admin_views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),

    path('password_change/',
         admin_views.PasswordChangeView.as_view(template_name='users/password_change.html'),
         name='password_change'),
    path('password_change/done/', admin_views.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'),
         name='password_change_done'),

    path('password_reset/',
         admin_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         admin_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         admin_views.PasswordResetConfirmView.as_view(template_name='users/reset.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         admin_views.PasswordResetCompleteView.as_view(template_name='users/reset_done.html'),
         name='password_reset_complete'),
]
