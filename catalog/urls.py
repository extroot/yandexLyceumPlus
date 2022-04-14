from catalog import views

from django.urls import path


urlpatterns = [
    path('<int:id_product>/', views.item_detail, name='item_detail'),
    path('', views.item_list, name='all_items'),
]
