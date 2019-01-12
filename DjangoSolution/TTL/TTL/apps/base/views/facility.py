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

def index(request):
    return HttpResponse("Hello, world. You're at the user index.")
    #return redirect('/base/facility.html')

