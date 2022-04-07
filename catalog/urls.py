from django.urls import path

from catalog import views

urlpatterns = [
    path('<int:id_product>/', views.item_detail, name='product_page'),
    path('', views.item_list, name='all_products'),
]
