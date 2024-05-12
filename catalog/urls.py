from django.urls import path

from catalog.views import home, contacts, ProductsListView, ProductView

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products_list/', ProductsListView.as_view(), name='products_list'),
    path('products_list/<int:pk>/', ProductView.as_view(), name='product_detail')
]