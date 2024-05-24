from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Product, Version
from django.views.generic import (
    CreateView, ListView, DetailView, DetailView, UpdateView, DeleteView)
from catalog.forms import ProductForm, VersionForm
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.forms.models import inlineformset_factory

# Create your views here.


def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

class ProductsCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name)
            new_product.save()

        return super().form_valid(form)

class ProductsUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name)
            new_product.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context["formset"] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context["formset"] = ProductFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context =  self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_success_url(self):
        return reverse('catalog:view', args=[self.kwargs.get('pk')])

class ProductsListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for object in context.get('object_list'):
            version = Version.objects.filter(current_version=True, product_id=object.pk).first()
            object.version = version
        return context


class ProductView(DetailView):
    model = Product

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

