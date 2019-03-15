from django import forms

from base.models import *

fancy = lambda: forms.TextInput(attrs={'class': 'derp'})



from django.forms import ModelForm



class ClientTypeForm(ModelForm):
    class Meta:
        model = ClientType
        fields = ['name',]


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name','type','primary_user',]

class AddressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if (field.widget.__class__ == forms.widgets.TextInput or field.widget.__class__ == forms.widgets.Select):
                if 'class' in field.widget.attrs:
                    #print(field.widget.attrs)
                    #print(field.widget.__class__)
                    #print(name)
                    field.widget.attrs['class'] += ' form-control'
                else:
                    #print(field.widget.attrs)
                    #print(field.widget.__class__)
                    #print(name)
                    field.widget.attrs.update({'class':'form-control'})
                    
    class Meta:
        model = Address
        fields = ['id', 'name', 'client', 'street_line1', 'street_line2', 'city', 'state', 'zipcode', 'country',]
        
"""

#class BookForm(ModelForm):
#    class Meta:
#        model = Book
#        fields = ['name', 'author']

#class BooknewForm(ModelForm):
#    class Meta:
#        model = Booknew
#        fields = ['name', 'author']
"""