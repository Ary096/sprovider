from django.urls import path
from .views import submit_review, add_review, service_reviews

urlpatterns = [
    path('submit/<int:booking_id>/', submit_review, name='submit_review'),
    path('review/<int:service_id>/', add_review, name='add_review'),
    path('service-reviews/<int:service_id>/', service_reviews, name='service_reviews'),
]
