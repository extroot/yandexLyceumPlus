from django.urls import path

from users import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile_page'),
    path('users/<int:id_user>/', views.user_detail, name='user_page'),
    path('users/', views.user_list, name='users_page'),
]
