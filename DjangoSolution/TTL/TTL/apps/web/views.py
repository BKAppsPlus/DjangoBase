from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'web/index.html',
        {
            'login':'kjhsk',
            'title':'Home Page',
            'year':datetime.now().year,
            'num_visits': num_visits,
        }
    )
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'web/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'web/about.html',
        {
            'title':'About This App',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the user index.")


