from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

from  django.views.generic import TemplateView

from TTL.apps.base.forms import FacilityForm


class HomeView(TemplateView):
    template_name = 'base/facility.html'
    
    def get(self, request):
        form = FacilityForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FacilityForm(request.POST)
        if form.is_valid():
            text =  form.cleaned_data['postField']
            form = FacilityForm()
            return redirect('base:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

def index(request):
    return HttpResponse("Hello, world. You're at the user index.")
    #return redirect('/base/facility.html')

