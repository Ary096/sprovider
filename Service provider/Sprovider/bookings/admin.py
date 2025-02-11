from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'status', 'created_at', 'payment_status', )
    list_filter = ('status',)
    search_fields = ('id', 'service__name', 'status',)
    ordering = ('-created_at',)

admin.site.register(Booking, BookingAdmin)