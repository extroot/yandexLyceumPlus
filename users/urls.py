from django.urls import path

from users import views

urlpatterns = [
    path('signup/', views.sighup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('recover/', views.sighup, name='password_recovery'),

    path('profile/', views.profile, name='profile_page'),
    path('users/<int:id_user>/', views.user_detail, name='user_page'),
    path('users/', views.user_list, name='all_users'),
]
