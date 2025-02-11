from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User,CustomerProfile, ProviderProfile


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'role']  # Remove 'username'

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'role']  # Removed first_name, last_name (these should be in profile forms)

class ProviderProfileForm(forms.ModelForm):
    class Meta:
        model = ProviderProfile
        fields = ['profile_picture', 'first_name', 'last_name', 'business_name', 'phone_number', 'address']

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['profile_picture', 'first_name', 'last_name', 'phone_number', 'address']
