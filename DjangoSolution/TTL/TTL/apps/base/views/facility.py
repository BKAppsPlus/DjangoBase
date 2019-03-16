from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse

from django.contrib.auth.models import User

# Create your views here.
from  django.views.generic import TemplateView
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
        form.instance.modified_by = self.request.user
        return super(BaseModelMixin, self).form_valid(form)
#ClientType Views
#region ClientType Views
class ClientTypeListView(ListView):
    model = ClientType

class ClientTypeCreateView(BaseModelMixin, CreateView):
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

class AddressesView(TemplateView):
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

def index(request):
    return HttpResponse("Hello, world. You're at the user index.")
    #return redirect('/base/facility.html')



class AddressIndexView(ListView):
    template_name = 'base/address_list.html'
    contect_object_Name = 'all_Addresses'

    def get_queryset(self):
        return Address.objects.all()

class AddressDetailView(DetailView):
    model=Address
    template_name = 'base/address.html'

class AddressCreateView0(CreateView):
    model=Address
    fields = [ 'name', 'client', 'street_line1', 'street_line2', 'city', 'state', 'zipcode', 'country',]

    def form_valid(self, form):
        print('asfasdfasdfasdfasfasdfasdfasdfasfasdfasdfasdfasfasdfasdfasdf')
        print('asfasdfasdfasdfasfasdfasdfasdfasfasdfasdfasdfasfasdfasdfasdf')
        print('asfasdfasdfasdfasfasdfasdfasdfasfasdfasdfasdfasfasdfasdfasdf')
        print(self.client)
        return super(AddressCreateView0, self).form_valid(form)


class AddressCreateViewold(CreateView):
  
    template_name = 'base/address_form.html'
    #fields = ['id', 'name', 'client', 'street_line1', 'street_line2', 'city', 'state', 'zipcode', 'country',]
    def get(self, request):
        form = AddressForm()
        args = {'form': form, }
        return render(request, self.template_name, args)
#######################################
#class ClientTypeIndexView(ListView):
#    template_name = 'base/clienttype_list.html'
#    contect_object_Name = 'all_ClientTypes'

#    def get_queryset(self):
#        return ClientType.objects.all()

#class ClientTypeDetailView(DetailView):
#    model = ClientType
#    template_name = 'base/clienttype.html'

#class ClientTypeCreateView(CreateView):
#    model = Client
#######################################    
#class AuditableMixin(object,):
#    def form_valid(self, form, ):
#        if not form.instance.id:
#            form.instance.created_by = self.request.user
#        form.instance.modified_by = self.request.user
#        return super(AuditableMixin, self).form_valid(form)

#class HomeTemplateView(TemplateView):
#    template_name = 'home.html'


#class BookCreateView(AuditableMixin, CreateView):
#    model = Book
#    form_class = BookForm

#class BookUpdateView(AuditableMixin, UpdateView):
#    model = Book
#    form_class = BookForm

#class BookListView(ListView):
#    model = Book

#class BooknewCreateView(BaseModelMixin, CreateView):
#    model = Booknew
#    form_class = BooknewForm

#class BooknewUpdateView(BaseModelMixin, UpdateView):
#    model = Booknew
#    form_class = BookForm

#class BooknewListView(ListView):
#    model = Booknew
