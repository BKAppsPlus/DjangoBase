from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.
from  django.views.generic import TemplateView

from TTL.apps.base.forms import AddressForm

from base.models import *


class HomeView(TemplateView):
    template_name = 'base/address.html'
    
    def get(self, request):
        form = AddressForm()
        addresses = Address.objects.all().order_by('-created')
        #print(addresses)
        
        args = {'form': form, 'addresses': addresses}
        return render(request, self.template_name, args)

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            addressform = form.save(commit=False)
            addressform.modified_by = request.user
            addressform.created_by = request.user
            #addressform.modified = 
            #addressform.created = request.user
            addressform.save()
            text =  form.cleaned_data['name']
            form = AddressForm()
            #return redirect('base:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

def index(request):
    return HttpResponse("Hello, world. You're at the user index.")
    #return redirect('/base/facility.html')

