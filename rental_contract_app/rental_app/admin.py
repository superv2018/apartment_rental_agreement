from django.contrib import admin
from .models import Landlord, RentalProperty

# Register your models here.
admin.site.register(Landlord)
admin.site.register(RentalProperty)