from catalog import views

from django.urls import path


urlpatterns = [
    path('<int:id_product>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('', views.ItemListView.as_view(), name='all_items'),
]
