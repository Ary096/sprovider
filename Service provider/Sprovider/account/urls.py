from django.urls import path
from .views import register_view, login_view, logout_view, dashboard_view, update_profile, home

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user_dashboard/', dashboard_view, name='user_dashboard'),
    path('update-profile/', update_profile, name='update_profile'),
]
