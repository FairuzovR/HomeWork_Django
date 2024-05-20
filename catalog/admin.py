from django.contrib import admin

from catalog.models import Product, Category, Version

# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'number_version', 'current_version',)
