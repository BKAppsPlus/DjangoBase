from django import forms
from django.forms import ModelForm

from .models import *

class PartyTypeForm(ModelForm):
    class Meta:
        model = PartyType
        fields = ['name',]


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name','type','primary_user',]

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'client', 'street_line1', 'street_line2', 'city', 'state', 'zipcode', 'country',]

    
