from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    scheduled_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        label="Select Booking Date"
    )

    class Meta:
        model = Booking
        fields = ['scheduled_date']
