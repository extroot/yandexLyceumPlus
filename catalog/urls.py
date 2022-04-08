from catalog import views

from django.urls import path


urlpatterns = [
    path('<int:id_product>/', views.item_detail, name='product_page'),
    path('', views.item_list, name='all_products'),
]
