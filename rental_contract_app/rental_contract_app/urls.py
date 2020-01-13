"""rental_contract_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'rental_app'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('property_list/<int:pk>/', views.PropertyDetailView.as_view(), name='detail'),
    path('property_update/<int:pk>/', views.PropertyUpdateView.as_view(), name='update'),
    path('new_property/', views.CreateNewPropertyView.as_view(), name='new_property'),
    path('property_list/', views.PropertyListView.as_view(), name='property_list'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/', views.TestPage.as_view(), name='test'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
    path('admin/', admin.site.urls),
]
