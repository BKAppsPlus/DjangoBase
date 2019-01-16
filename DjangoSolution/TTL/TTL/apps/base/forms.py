from django import forms
from base.models import *

fancy = lambda: forms.TextInput(attrs={'class': 'derp'})


class AddressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if (field.widget.__class__ == forms.widgets.TextInput or field.widget.__class__ == forms.widgets.Select):
                if 'class' in field.widget.attrs:
                    print(field.widget.attrs)
                    print(field.widget.__class__)
                    print(name)
                    #field.widget.attrs['class'] += ' form-control'
                else:
                    print(field.widget.attrs)
                    print(field.widget.__class__)
                    print(name)
                    field.widget.attrs.update({'class':'form-control'})
                    

    class Meta:
        model = Address
        fields = ('name', 'type', 'street_line1', 'street_line2', 'city', 'state', 'zipcode', 'country',)
        

