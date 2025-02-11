from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking, Notification
from services.models import Service
from .forms import BookingForm
from django.utils import timezone
from rest_framework import generics, permissions
from .serializers import NotificationSerializer


@login_required
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.service = service
            booking.booking_date = timezone.now()
            booking.status = 'pending'
            booking.payment_mode = 'COD'
            booking.payment_status = False
            booking.save()
            return redirect('booking_success')

    else:
        form = BookingForm()

    return render(request, 'bookings/book_service.html', {'service': service, 'form': form})

@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def provider_bookings(request):
    provider_services = Service.objects.filter(provider=request.user)
    bookings = Booking.objects.filter(service__in=provider_services).order_by('-created_at')
    return render(request, 'bookings/provider_bookings.html', {'bookings': bookings})

def booking_success(request):
    return render(request, 'bookings/booking_success.html')

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.status = 'cancelled'
    booking.save()
    return redirect('my_bookings')

@login_required
def provider_confirm_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, service__provider=request.user)
    booking.status = 'confirmed'
    booking.save()
    return redirect('provider_bookings')

@login_required
def provider_cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, service__provider=request.user)
    booking.status = 'cancelled'
    booking.save()
    return redirect('provider_bookings')

@login_required
def mark_booking_completed(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user, status='confirmed')
    booking.status = 'completed'
    booking.payment_status = True
    booking.save()
    return redirect('my_bookings')

# Notification API Views
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

class MarkNotificationAsReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user, is_read=False)

# Utility function
def send_notification(user, message):
    Notification.objects.create(recipient=user, message=message)