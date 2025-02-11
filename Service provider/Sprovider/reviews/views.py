from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bookings.models import Booking
from services.models import Service
from .forms import ReviewForm

@login_required
def submit_review(request, booking_id):
    # Safely retrieve the booking or return 404
    booking = get_object_or_404(Booking, id=booking_id, user=request.user, status='completed')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.service = booking.service  # Assuming Booking has a 'service' field
            review.save()
            return redirect('my_bookings')  # Ensure 'my_bookings' URL name exists
    else:
        form = ReviewForm()

    return render(request, 'reviews/submit_review.html', {'form': form, 'booking': booking})

@login_required
def add_review(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.service = service
            review.save()
            return redirect('service_reviews', service_id=service.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'service': service})

def service_reviews(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    reviews = service.reviews.all()
    return render(request, 'reviews/service_reviews.html', {'service': service, 'reviews': reviews})
