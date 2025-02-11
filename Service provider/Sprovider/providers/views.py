from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from bookings.models import Booking
from services.models import Service
from reviews.models import Review

@login_required
def provider_dashboard(request):
    services = Service.objects.filter(provider=request.user)
    bookings = Booking.objects.filter(service__provider=request.user)
    completed_bookings = Booking.objects.filter(service__provider=request.user, status='completed')
    reviews = Review.objects.filter(service__in=services)


    return render(request, 'providers/dashboard.html', {
        'services': services,
        'bookings': bookings,
        'completed_bookings': completed_bookings,
        'reviews': reviews,
        
    })

@login_required
def update_booking_status(request, booking_id, status):
    booking = get_object_or_404(Booking, id=booking_id, service__provider=request.user)
    if status in ['confirmed', 'cancelled']:
        booking.status = status
        booking.save()
    return redirect('provider_dashboard')
