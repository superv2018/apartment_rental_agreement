from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
from rental_app import models
from rental_app.forms import CreateNewPropertyForm
from django.urls import reverse_lazy 


class PropertyUpdateView(UpdateView):
    fields = ('address', 'social_security_number', 'email_address')
    model = models.Landlord

class PropertyDetailView(DetailView):
    context_object_name = 'property_detail'
    model = models.Landlord
    template_name = 'property_detail.html'

class CreateNewPropertyView(CreateView):
    model = models.Landlord
    form_class = CreateNewPropertyForm
    success_url = reverse_lazy('property_list')
    template_name = 'new_property.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateNewPropertyView, self).form_valid(form)

class PropertyListView(ListView):
    #landlord is name used in the for loop
    context_object_name = 'landlords'
    model = models.Landlord
    template_name = 'property_list.html'

class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(TemplateView):
    template_name = 'index.html'