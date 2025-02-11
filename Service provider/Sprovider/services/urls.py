from django.urls import path
from .views import service_list, add_service, service_detail

urlpatterns = [
    path('service_list/', service_list, name='service_list'),
    path('service_detail/<int:id>/', service_detail, name='service_detail'),
    path('add/', add_service, name='add_service'),
]
