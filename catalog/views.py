from django.shortcuts import render, get_object_or_404
from catalog.models import Product

# Create your views here.

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

def products_list(request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request, 'catalog/products_list.html', context)

def product_date(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product_date.html', context)