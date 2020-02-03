from django.urls import path
from rental_app import views

app_name = 'rental_app'
# Create your views here.

urlpatterns = [
    path('property_list/<int:pk>/', views.PropertyDetailView.as_view(), name='property_detail'),
    path('rental_update/<int:pk>/', views.RentalUpdateView.as_view(), name='rental_update'),
    path('landlord_update/<int:pk>/', views.LandlordUpdateView.as_view(), name='landlord_update'),
    path('new_apartment_info/', views.ApartmentBasicInfoView.as_view(), name='new_apartment_info'),
    path('delete<int:pk>/', views.PropertyDeleteView.as_view(), name='property_delete'),
    path('new_contract/', views.ContractView.as_view(), name='new_contract'),
    path('new_landlord/', views.CreateLandlordView.as_view(), name='new_landlord'),
    path('new_rental', views.CreateRentalView.as_view(), name='new_rental'),
    path('test/', views.TestPage.as_view(), name='test'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
    path('', views.HomePage.as_view(), name='home'),
    path('property_list/', views.PropertyListView.as_view(), name='property_list'),
]