from django.contrib import admin
from .models import Review
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'rating', 'created_at']
    search_fields = ['customer__first_name', 'service__name']
    list_filter = ['rating']