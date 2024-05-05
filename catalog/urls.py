from django.urls import path

from catalog.views import home, contacts, products_list, product_date

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products_list/', products_list, name='products_list'),
    path('products_list/<int:pk>/', product_date, name='product_date')
]