from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

#from TTL.apps.user.forms import (
#    RegistrationForm, 
#    EditProfileForm  
#    )
#from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request,'accounts/register.html', args)


def profile_view(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        print('qwdqwdqwdqwdqwdwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
        print(user)
    else:
        print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
        user = request.user
    args ={
        'user': user,
        'title':'About This App',
        'message':'Your application description page.',
        'year':datetime.now().year
        }
    return render(request, 'accounts/profile_view.html', args)



def profile_edit(request):
    err=''
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
       
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form,
                'title':'Edit Profile',
                'message':'Edit Profile page.',
                'err': err,}

        return render(request,'accounts/profile_edit.html', args)


def change_password(request):
    err=''
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
       
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile/')
        else:
            return redirect('accounts/password_change.html')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form,
                'title':'Change Password',
                'message':'Change Password page.',
                'err': err,}

        return render(request,'user/password_change.html', args)


"""
def profile(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'accounts/profile.html',
        {
            'title':'About This App',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
"""
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the user index.")
