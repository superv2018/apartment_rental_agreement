from django import forms
from . import models

class CreateLandlordForm(forms.ModelForm):
    class Meta:
        model = models.Landlord
        exclude = ['user']



class CreateRentalPropertyForm(forms.ModelForm):
    class Meta:
        model = models.RentalProperty
        exclude = ['landlord','created_by']

class CreateApartmentBasicInfoForm(forms.ModelForm):
    class Meta: 
        model = models.ApartmentBasicInfo
        exclude = ['apartment_pictures', 'video']

class CreateContractForm(forms.ModelForm):
    class Meta:
        model = models.Contract 
        exclude = ['_all_']


