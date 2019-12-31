'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Landlord(models.Model):
    address = models.CharField(max_length=255)
    social_security_number = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)


class rentalProperty(models.Model):
    landlord = models.ForeignKey("Landlord", on_delete=models.PROTECT)
    PROPERTY_LISTING_CHOICES = [
        (APARTMENT, 'Apartment'),
        (HOLIDAY_HOME, 'Holiday home'),
        (SINGLE_FAMILY_HOME, 'Single family home'),
        (COMMERCIAL, 'Commercial'),
    ]
    type_of_property_listing = models.CharField(
        max_length = 50,
        choices = PROPERTY_LISTING_CHOICES,
        default = APARTMENT
    )
    BUILDING_LISTING_CHOICES = [
        (CONDOMINIUM, 'Condominium'),
        (ROW_HOUSE, 'Row house'),
        (SINGLE_FAMILY_HOUSE, 'Single family house'),
        (HOLIDAY_HOME, 'Holiday_home'),
        (DUPLEX, 'Duplex'),
        (SINGLE_FAMILY_HOME_COOP, 'Single family home(CO-OP)'),
        (CONDOMINIUM_EXTERNAL_ENTRANCE, 'Condominium external entrance'),
        (WOODEN_COMDOMINIUM_HOUSE, 'Wooden condominium house')
    ]
    type_of_building_choices = models.CharField(
        max_length = 50,
        choices = BUILDING_LISTING_CHOICES,
        default = CONDOMINIUM
    )
    created_by = models.ForeignKey(User, related_name='rentalProperties')

class Location(models.Model):
    rental_property = models.ForeignKey("rentalProperty", on_delete=models.PROTECT)
    street = models.CharField(max_length=255)
    borough = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class ApartmentBasicInfo(models.Model):
    location = models.ForeignKey("Location", on_delete=models.PROTECT)
    title = models.TextField()
    living_area = models.IntegerField()
    number_of_rooms = models.IntegerField()
    floors = models.IntegerField()
    furnished = models.BooleanField(initial=True)
    KITCHEN_TYPE_CHOICES = [
        (UNKNOWN, 'Unknown'),
        (NO_KITCHEN, 'No kitchen'),
        (KITCHEN, 'Kitchen'),
        (MINI_KITCHEN, 'Mini kitchen'),
        (OPEN_KITCHEN, 'Open kitchen')
    ]
    type_of_kitchen_choices = models.CharField(
        max_length = 50,
        choices = KITCHEN_TYPE_CHOICES,
        default = UNKNOWN
    ) 
    sauna = models.BooleanField(initial=True)
    balcony = models.BooleanField(initial=True)
    apartment_layout_type = models.IntegerField()
    APARTMENT_CONDITIONS_CHOICES = [
        (EXCELLENT, 'excellent'),
        (GOOD, 'good'),
        (FAIR, 'fair'),
        (POOR, 'poor'),
        (VERY_BAD, 'very bad')
    ]
    apartment_condition = models.CharField(
        max_length = 50,
        choices = APARTMENT_CONDITIONS_CHOICES,
        default = EXCELLENT
    )
    apartment_conditions_freetext = models.TextField()




class Contract(models.Model):
    rentalproperty = models.ForeignKey("rentalProperty", on_delete=models.PROTECT)
    RENTAL_TERMS_CHOICES = [
        (PERMANENT, 'permanent'),
        (FiXED, 'fixed'),
    ]
    type_of_rental_terms = models.CharField(
        max_length = 20,
        choices = RENTAL_TERMS_CHOICES,
        default = PERMANENT
    ) 
    rent_availability = models.DateField()
    rent_availability_info = models.TextField()
    rent_per_month = models.IntegerField()
    deposit_for_rent = models.IntegerField()
    deposit_for_rent_info = models.TextField()
    rental_increment = models.IntegerField()
    index_value = models.IntegerField()
    index_date = models.DateField()
    RENT_ELECTRICITY_CHOICES = [
        (UNDEFINED, 'undefined'),
        (INCLUDED_IN_THE_RENT, 'included in the rent'),
        (RESPONSIBILITY_OF_TENANT, 'responsibility of tenant'),
        (FIXED_FEE, 'fixed fee'),
        (OTHER, 'other')
    ]
    rent_electricity = models.CharField(
        max_length = 50,
        choices = RENTAL_TERMS_CHOICES,
        default = UNDEFINED
    )
    electricity_fixed_fee = models.IntegerField()
    WATER_FEE_CHOICES = [
        (UNDEFINED, 'undefined'),
        (INCLUDED_IN_THE_RENT, 'included in the rent'),
        (RESPONSIBILITY_OF_TENANT, 'responsibility of tenant'),
        (FIXED_FEE_PER_PERSON, 'fixed fee per person'),
        (OTHER, 'other')
    ]
    water_fee = models.CharField(
        max_length = 50,
        choices = WATER_FEE_CHOICES,
        default = UNDEFINED
    )
    water_fee_per_person = models.IntegerField()
    HEATING_FEE_CHOICES = [
         (UNDEFINED, 'undefined'),
        (INCLUDED_IN_THE_RENT, 'included in the rent'),
        (RESPONSIBILITY_OF_TENANT, 'responsibility of tenant'),
        (FIXED_FEE, 'fixed fee'),
        (OTHER, 'other')
    ]
    heating_fee = models.CharField(
        max_length = 50,
        choices = HEATING_FEE_CHOICES,
        default = UNDEFINED
    )
    heating_fixed_fee = models.IntegerField()
    Other_cost = models.TextField()
    pets_allowed = models.BooleanField(initial=True)
    smoking_allowed = models.BooleanField(initial=True)
    insurance_required = models.BooleanField(initial=True)
    other_terms = models.TextField()

class Media(models.Nodel):
    apartment_pictures = models.ImageField()
    videos = models.CharField(max_length=512)
    virtual_tours = models.CharField(max_length=512)
'''