from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

class ProductsListView(ListView):
    model = Product
    # template_name = 'catalog/product_list.html'

class ProductView(DetailView):
    model = Product
