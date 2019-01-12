from django import forms


class FacilityForm(forms.Form):
    post = forms.CharField()