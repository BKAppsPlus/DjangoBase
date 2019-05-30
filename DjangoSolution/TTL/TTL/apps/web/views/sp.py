from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from TTL.apps.base.models.core import *

from django.views.generic import TemplateView
from django.views.generic.edit import (FormView,CreateView,UpdateView,DeleteView)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic.base import ContextMixin

class base_sp_Mixin(LoginRequiredMixin,  object, ):
    current_user = None
    site_client_type = ClientType.objects.get(name='SERVICE PROVIDER')
    
    def get_context_data(self, **kwargs):
        context = super(base_sp_Mixin, self).get_context_data(**kwargs)
        context.update(dict(current_user=self.request.user, site_client_type = ClientType.objects.get(name='SERVICE PROVIDER') ))
        return context

    def __init__(self):
        current_user=self.request.user
        site_client_type =ClientType.objects.get(name='SERVICE PROVIDER') 

#ClientType Views
#region ClientType Views
class ClientTypeListView(base_sp_Mixin,ListView):
    model = ClientType
    #.objects.filter(name='SERVICE PROVIDER')

class ClientTypeDetailView(base_sp_Mixin,DetailView):
    model = ClientType
#endregion

#Client Views
#region Client Views
class ClientListView(base_sp_Mixin, ListView):
    model = Client
    def get_queryset(self):
        print(base_sp_Mixin.site_client_type)
        print(base_sp_Mixin.current_user)
        myClients = Client.objects.filter(primary_user=base_sp_Mixin.current_user, type = base_sp_Mixin.site_client_type)
        return myClients

    def __init__(self):
        super()



class ClientDetailView(base_sp_Mixin, CreateView):
    model = Client


def index(request):
    # TEST
    return HttpResponse("Hello, world. You're at the SP index.")

def home(request):
    # TEST
    return HttpResponse("Hello, world. You're at the SP Home.")

def home1(request):
    # TEST
    return HttpResponse("Hello, world. You're at the SP Home.")
