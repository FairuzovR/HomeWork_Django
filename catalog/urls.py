from django.urls import path

from catalog.views import (home, contacts, ProductsCreateView,
                           ProductsUpdateView, ProductsListView, ProductView, ProductDeleteView)

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products_list/', ProductsListView.as_view(), name='products_list'),
    path('create/', ProductsCreateView.as_view(), name='create'),
    path('products_list/<int:pk>/', ProductView.as_view(), name='view'),
    path('edit/<int:pk>/', ProductsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]