from django import forms
from django.contrib.auth import get_user_model


class CustomUserUpdationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'phone', 'street_address', 'city', 'zip_code', 'secondary_contact']