from django.db import models
from django.conf import settings
from services.models import Service
from django.utils import timezone
from datetime import timedelta
from account.models import User
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(default=timezone.now)
    scheduled_date = models.DateTimeField(default=timezone.now() + timedelta(days=1))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    payment_mode = models.CharField(max_length=50, default='COD')  # Always set to COD
    payment_status = models.BooleanField(default=False)  # False until completed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.service.name} by {self.user.email}"


class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient} - {self.message[:50]}"