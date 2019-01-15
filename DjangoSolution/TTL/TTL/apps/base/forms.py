from django import forms


class FacilityForm(forms.Form):
    postField = forms.CharField(required=False)