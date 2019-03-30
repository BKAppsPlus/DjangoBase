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

class BaseModelMixin(object,):
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
class ClientTypeListView(ListView):
    model = ClientType

class ClientTypeCreateView(LoginRequiredMixin, BaseModelMixin, CreateView):
    model = ClientType
    form_class = ClientTypeForm

class ClientTypeDetailView(BaseModelMixin, UpdateView):
    model = ClientType
    form_class = ClientTypeForm


#endregion
#Client Views
#region Client Views
class ClientListView(ListView):
    model = Client

class ClientCreateView(BaseModelMixin, CreateView):
    model = Client
    form_class = ClientForm
    
class ClientDetailView(BaseModelMixin, UpdateView):
    model = Client
    form_class = ClientForm
#endregion

#Address Views
#region Address Views

class AddressListView(ListView):
    model = Address

class AddressCreateView(BaseModelMixin, CreateView):
    model = Address
    form_class = AddressForm
    
class AddressDetailView(BaseModelMixin, UpdateView):
    model = Address
    form_class = AddressForm


#endregion

class CurrentClient(TemplateView):    
    template_name = "base/curr.html"
    def get(self, request, pk):
        form = ClientForm()
        clients = Client.objects.get(id=1)
        allUsers = User.objects.all().order_by('-id')
        print(clients)
        args = {'form': form, 'clients': clients, 'allUsers': allUsers  } #'address': address, 
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

#Obsolete
#region Obsolete

#class AddressCreateViewhuwuygwueyfg(CreateView):
#    model=Address
#    fields = [ 'name', 'client', 'street_line1', 'street_line2', 'city', 'state', 'zipcode', 'country',]

#    def form_valid(self, form):
#        print('asfasdfasdfasdfasfasdfasdfasdfasfasdfasdfasdfasfasdfasdfasdf')
#        print(self.client)
#        return super(AddressCreateView0, self).form_valid(form)


#class AddressCreateViewold(CreateView):
  
#    template_name = 'base/address_form.html'
#    #fields = ['id', 'name', 'client', 'street_line1', 'street_line2', 'city', 'state', 'zipcode', 'country',]
#    def get(self, request):
#        form = AddressForm()
#        args = {'form': form, }
#        return render(request, self.template_name, args)
#endregion
