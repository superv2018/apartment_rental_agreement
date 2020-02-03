from django.views.generic import (TemplateView, 
ListView, CreateView, DetailView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from rental_app.models import (Landlord, RentalProperty,
                                              Contract,
                                    ApartmentBasicInfo)
from rental_app.forms import (CreateLandlordForm, 
                             CreateRentalPropertyForm,
                             CreateApartmentBasicInfoForm,
                             CreateContractForm)
from django.urls import reverse_lazy 
from django.shortcuts import get_object_or_404



class RentalUpdateView(UpdateView):

    model = RentalProperty
    form_class = CreateRentalPropertyForm
    template_name = 'new_rental.html'
    

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
class PropertyDeleteView(DeleteView):
    model = Landlord
    success_url = reverse_lazy('property_list')
    


class LandlordUpdateView(UpdateView):
    model = Landlord
    form_class = CreateLandlordForm
    template_name = 'new_landlord.html'
   

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PropertyDetailView(DetailView):
    #context_object_name = 'property_detail'
    template_name = 'property_detail.html'
    model = ApartmentBasicInfo

    
    def get_context_data(self, **kwargs):
        context = super(PropertyDetailView, self).get_context_data(**kwargs)
        context['landlord_list'] = Landlord.objects.all()
        context['rentalproperty_list'] = RentalProperty.objects.all()
        context['apartmentbasicinfo_list'] = ApartmentBasicInfo.objects.all()
        context['contract_list'] = Contract.objects.all()
        return context

class CreateLandlordView(LoginRequiredMixin, CreateView):
    model = Landlord
    form_class = CreateLandlordForm
    template_name = 'new_landlord.html'
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    #def form_valid(self, form):
        #form.instance.user = self.request.user
        #return super(CreateLocationView, self).form_valid(form)

class CreateRentalView(CreateView):

    model = RentalProperty
    form_class = CreateRentalPropertyForm
    template_name = 'new_rental.html'
    

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    

class ApartmentBasicInfoView(CreateView):
    model = ApartmentBasicInfo
    form_class = CreateApartmentBasicInfoForm
    template_name = 'new_apartment_info.html'
    

class ContractView(CreateView):
    model = Contract
    form_class = CreateContractForm
    template_name = 'new_contract.html'
    



class PropertyListView(ListView):
    model = ApartmentBasicInfo
    template_name = 'property_list.html'
 
    #get current user
    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(rental_property__created_by=self.request.user).order_by('-id')
        
   

class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(TemplateView):
    template_name = 'index.html'