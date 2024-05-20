from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Version
from django.views.generic import (
    CreateView, ListView, DetailView, DetailView, UpdateView, DeleteView)
from catalog.forms import ProductForm
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.shortcuts import get_object_or_404, redirect

# Create your views here.


def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

class ProductsCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')

class ProductsUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # success_url = reverse_lazy('blogs:list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name)
            new_product.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view', args=[self.kwargs.get('pk')])

class ProductsListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["version"] = Version.objects.filter(current_version=True).first()
        for object in context.get('object_list'):
            version = Version.objects.filter(current_version=True, product_id=object.pk).first()
            object.version = version
            print(object.version)
            # product.version = product.version_set.filter(is_active=True).first()
        return context


class ProductView(DetailView):
    model = Product

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

