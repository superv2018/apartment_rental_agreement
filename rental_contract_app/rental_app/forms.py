from django import forms
from .models import Landlord

class CreateNewPropertyForm(forms.ModelForm):
    class Meta:
        model = Landlord
        fields = ['address', 'social_security_number', 'email_address']