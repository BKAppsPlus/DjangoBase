from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.edit import (FormView,CreateView,UpdateView,DeleteView)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from TTL.apps.base.forms import AddressForm, ClientTypeForm,ClientForm
#from TTL.apps.base.forms import BookForm, BooknewForm

from base.models import *

class BaseModelMixin(LoginRequiredMixin, object,):
    def form_valid(self, form, ):
        if not form.instance.id:
            form.instance.created_by = self.request.user
            print("asfasfasfasfasf")
        form.instance.modified_by = self.request.user
        return super(BaseModelMixin, self).form_valid(form)
    
   

def index(request):
    # TEST
    return HttpResponse("Hello, world. You're at the user index.")

#ClientType Views
#region ClientType Views
class ClientTypeListView(BaseModelMixin,ListView):
    model = ClientType

class ClientTypeDetailView(BaseModelMixin,DetailView):
    model = ClientType
    
class ClientTypeCreateView( BaseModelMixin, CreateView):
    model = ClientType
    form_class = ClientTypeForm

class ClientTypeUpdateView(BaseModelMixin, UpdateView):
    model = ClientType
    form_class = ClientTypeForm


#endregion

#Client Views
#region Client Views
class ClientListView(BaseModelMixin, ListView):
    model = Client

class ClientCreateView(BaseModelMixin, CreateView):
    model = Client
    form_class = ClientForm

class ClientDetailView(BaseModelMixin, DetailView):
    model = Client
    form_class = ClientForm


class CurrClientDetailView(BaseModelMixin, ListView):
    model = Client
    def get_queryset(self):
        return Client.objects.filter(primary_user=self.request.user)
    form_class = ClientForm

class ClientUpdateView(BaseModelMixin, UpdateView):
    model = Client


#endregion

#Address Views
#region Address Views

class AddressListView(BaseModelMixin, ListView):
    model = Address

class AddressCreateView(BaseModelMixin, CreateView):
    model = Address
    form_class = AddressForm
    
class AddressDetailView(BaseModelMixin, UpdateView):
    model = Address
    form_class = AddressForm


#endregion

class MyStuff(LoginRequiredMixin, TemplateView):    
    template_name = "base/mystuff.html"
    def get(self, request):
        form = ClientForm()
        allUsers = User.objects.filter(username=request.user.username)
        
        
        allClients = Client.objects.filter(primary_user=request.user)
        
        #allClientTypes = ClientType.objects.all().order_by('id')
        allClientTypes = ClientType.objects.filter(client__in=allClients).distinct()

        allAddresses = Address.objects.filter(client__in=allClients)
        #allAddresses = allClients[0].clientAddresses.all()

        
        #allFacilities= Facility.objects.all().order_by('name')
        allFacilities= Facility.objects.filter(client__in=allClients)

        #allFacilitySpaces= FacilitySpace.objects.all().order_by('name')
        allFacilitySpaces= FacilitySpace.objects.filter(facility__in=allFacilities)

        allTeachers= Teacher.objects.all().order_by('name')
        allHousehold= Household.objects.all().order_by('name')
        allHouseholdMemberships= HouseholdMembership.objects.all().order_by('name')
        
        
        args = {'form': form, 
                'allUsers': allUsers ,
                'allClients': allClients ,
                'allClientTypes': allClientTypes ,
                'allAddresses': allAddresses ,
                'allFacilities': allFacilities ,
                'allFacilitySpaces': allFacilitySpaces ,
                'allTeachers': allTeachers ,
                'allHousehold': allHousehold ,
                'allHouseholdMemberships': allHouseholdMemberships ,
                
                }  
        return render(request, self.template_name, args)

class AllStuff(LoginRequiredMixin, TemplateView):    
    template_name = "base/allstuff.html"
    def get(self, request):
        form = ClientForm()
        allUsers = User.objects.all().order_by('id')
        allClients = Client.objects.all().order_by('id')
        allClientTypes = ClientType.objects.all().order_by('id')
        allAddresses = Address.objects.all().order_by('id')
        allFacilities= Facility.objects.all().order_by('name')
        allFacilitySpaces= FacilitySpace.objects.all().order_by('name')
        allTeachers= Teacher.objects.all().order_by('name')
        allHousehold= Household.objects.all().order_by('name')
        allHouseholdMemberships= HouseholdMembership.objects.all().order_by('name')

        args = {'form': form, 
                'allUsers': allUsers ,
                'allClients': allClients ,
                'allClientTypes': allClientTypes ,
                'allAddresses': allAddresses ,
                'allFacilities': allFacilities ,
                'allFacilitySpaces': allFacilitySpaces ,
                'allTeachers': allTeachers ,
                'allHousehold': allHousehold ,
                'allHouseholdMemberships': allHouseholdMemberships ,
                
                } 
        return render(request, self.template_name, args)


class HomeView(TemplateView):
    template_name = 'base/home.html'
    
    def get(self, request):
        form = AddressForm()
        addresses = Address.objects.all().order_by('id')
        allUsers = User.objects.all().order_by('-id')
        print(self.args)
        #if pk:
        #    address = Address.objects.get(pk=pk)
        #    print('address received')
        
        
        args = {'form': form, 'addresses': addresses, 'allUsers': allUsers } #'address': address, 
        return render(request, self.template_name, args)

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            addressform = form.save(commit=False)
            addressform.modified_by = request.user
            addressform.created_by = request.user
            addressform.save()
            text =  form.cleaned_data['name']
            form = AddressForm()
            #return redirect('base:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

