
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from PIL import Image
from django.urls import reverse

# Create your models here.

UserModel = get_user_model()

class Landlord(models.Model):
    user = models.ForeignKey(UserModel, related_name='landlords', on_delete=models.PROTECT)
    address = models.CharField(max_length=255)
    social_security_number = models.CharField(max_length=255)
    email_address = models.EmailField()

    

    def __str__(self):
        return self.address


class RentalProperty(models.Model):
    landlord = models.ForeignKey("Landlord", related_name='rentalproperty', on_delete=models.PROTECT)
    created_by = models.ForeignKey(UserModel, related_name='rentalproperty', on_delete=models.PROTECT)

    PROPERTY_LISTING_CHOICES = Choices(
        ('APARTMENT', _('Apartment')),
        ('HOLIDAY_HOME', _('Holiday home')),
        ('SINGLE_FAMILY_HOME', _('Single family home')),
        ('COMMERCIAL', _('Commercial')),
    )
    type_of_property_listing = models.CharField(
        max_length = 50,
        choices = PROPERTY_LISTING_CHOICES,
        default = PROPERTY_LISTING_CHOICES.APARTMENT,
    )
    BUILDING_LISTING_CHOICES = Choices(
        ('CONDOMINIUM', _('Condominium')),
        ('ROW_HOUSE', _('Row house')),
        ('SINGLE_FAMILY_HOUSE', _('Single family house')),
        ('HOLIDAY_HOME', _('Holiday_home')),
        ('DUPLEX', _('Duplex')),
        ('SINGLE_FAMILY_HOME_COOP', _('Single family home(CO-OP)')),
        ('CONDOMINIUM_EXTERNAL_ENTRANCE', _('Condominium external entrance')),
        ('WOODEN_COMDOMINIUM_HOUSE', _('Wooden condominium house'))
    )
    type_of_building_choices = models.CharField(
        max_length = 50,
        choices = BUILDING_LISTING_CHOICES,
        default = BUILDING_LISTING_CHOICES.CONDOMINIUM,
    )
    
    street = models.CharField(max_length=255)
    borough = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.street

class ApartmentBasicInfo(models.Model):
    rental_property = models.ForeignKey("RentalProperty", null=True, related_name='basic_info', on_delete=models.PROTECT)
    title = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    living_area = models.PositiveIntegerField()
    number_of_rooms = models.PositiveIntegerField()
    floors = models.PositiveIntegerField()
    furnished = models.BooleanField(default=True)
    KITCHEN_TYPE_CHOICES = Choices(
        ('UNKNOWN', _('Unknown')),
        ('NO_KITCHEN', _('No kitchen')),
        ('KITCHEN', _('Kitchen')),
        ('MINI_KITCHEN', _('Mini kitchen')),
        ('OPEN_KITCHEN', _('Open kitchen'))
    )
    type_of_kitchen_choices = models.CharField(
        max_length = 50,
        choices = KITCHEN_TYPE_CHOICES,
        default = KITCHEN_TYPE_CHOICES.UNKNOWN,
    ) 
    sauna = models.BooleanField(default=True)
    balcony = models.BooleanField(default=True)
    apartment_layout_type = models.PositiveIntegerField()
    APARTMENT_CONDITIONS_CHOICES = Choices(
        ('EXCELLENT', 'excellent'),
        ('GOOD', _('good')),
        ('FAIR', _('fair')),
        ('POOR', _('poor')),
        ('VERY_BAD', _('very bad'))
    )
    apartment_condition = models.CharField(
        max_length = 50,
        choices = APARTMENT_CONDITIONS_CHOICES,
        default = APARTMENT_CONDITIONS_CHOICES.EXCELLENT,
    )
    apartment_conditions_freetext = models.TextField()
    apartment_pictures = models.ImageField(upload_to="images", null=False)
    video = models.URLField(max_length=250)

    

    def __str__(self):
        return self.title


class Contract(models.Model):
    rental_property = models.ForeignKey("RentalProperty", null=True, related_name='contracts', on_delete=models.PROTECT)
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT)
    RENTAL_TERMS_CHOICES = Choices(
        ('PERMANENT', _('permanent')),
        ('FiXED', _('fixed')),
    )
    type_of_rental_terms = models.CharField(
        max_length = 20,
        choices = RENTAL_TERMS_CHOICES,
        default = RENTAL_TERMS_CHOICES.PERMANENT,
    ) 
    rent_availability = models.DateField()
    rent_availability_info = models.TextField(blank=True)
    rent_per_month = models.IntegerField()
    deposit_for_rent = models.IntegerField()
    deposit_for_rent_info = models.TextField(blank=True)
    rental_increment = models.IntegerField(blank=True)
    index_value = models.IntegerField(blank=True)
    index_date = models.DateField(blank=True)
    RENT_ELECTRICITY_CHOICES = Choices(
        ('UNDEFINED', _('undefined')),
        ('INCLUDED_IN_THE_RENT', _('included in the rent')),
        ('RESPONSIBILITY_OF_TENANT', _('responsibility of tenant')),
        ('FIXED_FEE', _('fixed fee')),
        ('OTHER', _('other'))
    )
    rent_electricity = models.CharField(
        max_length = 50,
        choices = RENT_ELECTRICITY_CHOICES,
        default = RENT_ELECTRICITY_CHOICES.UNDEFINED,
    )
    electricity_fixed_fee = models.IntegerField()
    WATER_FEE_CHOICES = Choices(
        ('UNDEFINED', _('undefined')),
        ('INCLUDED_IN_THE_RENT', _('included in the rent')),
        ('RESPONSIBILITY_OF_TENANT', _('responsibility of tenant')),
        ('FIXED_FEE_PER_PERSON', _('fixed fee per person')),
        ('OTHER', _('other'))
    )
    water_fee = models.CharField(
        max_length = 50,
        choices = WATER_FEE_CHOICES,
        default = WATER_FEE_CHOICES.UNDEFINED,
    )
    water_fee_per_person = models.IntegerField()
    HEATING_FEE_CHOICES = Choices(
         ('UNDEFINED', _('undefined')),
        ('INCLUDED_IN_THE_RENT', _('included in the rent')),
        ('RESPONSIBILITY_OF_TENANT', _('responsibility of tenant')),
        ('FIXED_FEE', _('fixed fee')),
        ('OTHER', _('other'))
    )
    heating_fee = models.CharField(
        max_length = 50,
        choices = HEATING_FEE_CHOICES,
        default = HEATING_FEE_CHOICES.UNDEFINED,
    )
    heating_fixed_fee = models.IntegerField()
    Other_cost = models.TextField(blank=True)
    pets_allowed = models.BooleanField(default=True)
    smoking_allowed = models.BooleanField(default=True)
    insurance_required = models.BooleanField(default=True)
    other_terms = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('rental_app:property_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.rent_availability


    
    



