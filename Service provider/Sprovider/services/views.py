from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q  # Fix for filtering issue
from .models import Service, Category
from .forms import ServiceForm
from reviews.models import Review
from bookings.models import Booking

def service_list(request):
    query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    min_rating = request.GET.get('min_rating', '')

    services = Service.objects.all()

    if query:
        services = services.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if category_filter:
        services = services.filter(category__name=category_filter)

    if min_price and max_price:
        services = services.filter(price__gte=min_price, price__lte=max_price)

    if min_rating:
        services = services.filter(average_rating__gte=min_rating)

    categories = Category.objects.all()

    return render(request, 'services/service_list.html', {
        'services': services,
        'categories': categories,
        'query': query,
        'category_filter': category_filter,
    })

def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    reviews = Review.objects.filter(service=service).order_by('-created_at')

    has_completed_booking = False
    if request.user.is_authenticated and request.user.is_customer:
        has_completed_booking = Booking.objects.filter(service=service, user=request.user, status='completed').exists()

    return render(request, 'services/service_detail.html', {
        'service': service,
        'reviews': reviews,
        'has_completed_booking': has_completed_booking,
    })

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)  # Fix: Include request.FILES
        if form.is_valid():
            service = form.save(commit=False)
            service.provider = request.user
            service.save()
            return redirect('provider_dashboard')
    else:
        form = ServiceForm()
    return render(request, 'services/add_service.html', {'form': form})
