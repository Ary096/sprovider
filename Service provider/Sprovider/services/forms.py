from django import forms
from .models import Service, Category

class ServiceForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    tags = forms.CharField(required=False, help_text="Enter comma-separated tags (e.g., 'plumbing, repair, home')")

    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'category', 'tags']
