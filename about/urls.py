from about import views

from django.urls import path

urlpatterns = [
    path('', views.DescriptionView.as_view(), name='about')
]
