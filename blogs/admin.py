from django.contrib import admin
from blogs.models import Blog

@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'views_count', 'time_create',)
    list_filter = ('is_published',)
    search_fields = ('title',)
