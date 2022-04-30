from django.urls import path

from users import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('profile/', views.ProfileView.as_view(), name='profile_page'),
    path('users/<int:id_user>/', views.UserDetailView.as_view(), name='user_page'),
    path('users/', views.UserListView.as_view(), name='all_users'),

    path(
        'login/',
        views.LoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        'password_change/',
        views.PasswordChangeView.as_view(),
        name='password_change'
    ),
    path(
        'password_change/done/',
        views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),

    path(
        'password_reset/',
        views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
