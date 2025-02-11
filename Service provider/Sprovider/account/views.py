from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomerProfile, ProviderProfile
from services.models import Service, Category
from .forms import UserRegistrationForm, CustomerProfileForm, ProviderProfileForm
from bookings.models import Booking
from providers.views import provider_dashboard
def home(request):
    category = Category.objects.all()
    all_services = Service.objects.all()  # Fetch all services
    category_services = {}  # Dictionary for category-wise services

    # Fetch services grouped by category
    categories = Service.objects.values_list('category', flat=True).distinct()
    for category in categories:
        category_services[category] = Service.objects.filter(category=category)

    context = {
        'all_services': all_services,
        'category_services': category_services
    }
    return render(request, 'index.html', context)

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect if already logged in

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect_dashboard(request.user)  # Redirect based on role

    error = None
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user:
            login(request, user)
            return redirect_dashboard(user)  # Redirect based on role
        else:
            error = "Invalid email or password"
    
    return render(request, 'account/login.html', {'error': error})

def redirect_dashboard(user):
    """Redirect user based on role"""
    if user.role == "customer":
        return redirect("user_dashboard")
    elif user.role == "provider":
        return redirect("provider_dashboard")
    else:
        return redirect("login") 
    
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    recent_bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')[:5]
    return render(request, 'account/dashboard.html', {'user': request.user, 'recent_bookings': recent_bookings,})


@login_required
def update_profile(request):
    user = request.user
    provider_form = None
    customer_form = None

    if user.role == 'provider':
        profile = ProviderProfile.objects.get(user=user)
        if request.method == 'POST':
            provider_form = ProviderProfileForm(request.POST, request.FILES, instance=profile)
            if provider_form.is_valid():
                provider_form.save()
                messages.success(request, "Profile updated successfully!")
                return redirect('update_profile')  # Redirect to refresh the page
        else:
            provider_form = ProviderProfileForm(instance=profile)

    elif user.role == 'customer':
        profile = CustomerProfile.objects.get(user=user)
        if request.method == 'POST':
            customer_form = CustomerProfileForm(request.POST, request.FILES, instance=profile)
            if customer_form.is_valid():
                customer_form.save()
                messages.success(request, "Profile updated successfully!")
                return redirect('update_profile')
        else:
            customer_form = CustomerProfileForm(instance=profile)

    return render(request, 'account/update_profile.html', {
        'provider_form': provider_form,
        'customer_form': customer_form
    })