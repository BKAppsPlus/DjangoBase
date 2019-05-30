from django import forms

from TTL.apps.base.models import *

from django.forms import ModelForm

class ClientTypeForm(ModelForm):
    class Meta:
        model = ClientType
        fields = ['name',]


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name','type','primary_user',]

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'client', 'street_line1', 'street_line2', 'city', 'state', 'zipcode', 'country',]

    
