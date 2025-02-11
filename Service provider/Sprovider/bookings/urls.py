from django.urls import path
from .views import (
    book_service, booking_success, cancel_booking,
    mark_booking_completed, user_bookings, provider_bookings,
    provider_confirm_booking, provider_cancel_booking,
    NotificationListView, MarkNotificationAsReadView
)

urlpatterns = [
    # Booking URLs
    path('book/<int:service_id>/', book_service, name='book_service'),
    path('booking-success/', booking_success, name='booking_success'),
    path('my-bookings/', user_bookings, name='user_bookings'),
    
    # User booking actions
    path('cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('complete/<int:booking_id>/', mark_booking_completed, name='mark_booking_completed'),
    
    # Provider booking actions
    path('provider/bookings/', provider_bookings, name='provider_bookings'),
    path('provider/confirm/<int:booking_id>/', provider_confirm_booking, name='provider_confirm_booking'),
    path('provider/cancel/<int:booking_id>/', provider_cancel_booking, name='provider_cancel_booking'),
    
    # Notification URLs
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/mark-read/<int:pk>/', MarkNotificationAsReadView.as_view(), name='mark-notification-read'),
]