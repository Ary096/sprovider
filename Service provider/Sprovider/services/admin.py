from django.contrib import admin
from .models import Service, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'provider', 'category', 'price', 'average_rating')
    list_filter = ('category', 'price', 'average_rating')
    search_fields = ('name', 'description', 'tags')
    ordering = ('-average_rating',)
