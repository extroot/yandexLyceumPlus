from about import views

from django.urls import path


urlpatterns = [
    path('', views.description, name='about_page')
]
