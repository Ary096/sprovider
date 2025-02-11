from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ProviderProfile, CustomerProfile

# Custom UserAdmin
class CustomUserAdmin(UserAdmin):
    list_display = ('id','email', 'is_provider', 'is_customer', 'date_joined')
    list_filter = ('role', 'is_staff', 'is_superuser')  # Use 'role' instead of 'is_provider' and 'is_customer'
    search_fields = ('email'),
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'profile_picture', 'gender', 'address')}),
        ('Roles', {'fields': ('role', 'is_staff', 'is_superuser')}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

# Register models
admin.site.register(User, CustomUserAdmin)
admin.site.register(ProviderProfile)
admin.site.register(CustomerProfile)
