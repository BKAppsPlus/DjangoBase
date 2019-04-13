
from django.conf.urls import url, include
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms

from TTL.apps.web import views
import TTL.apps.accounts.views

 
from . import views

app_name = 'web'

urlpatterns = [
    re_path(r'^Behzad_test0_Path', views.index, name='index'), #/accounts/Behzad_test0_PathABCDEFGHI
    re_path(r'^Behzad_test1_Path/$', views.index, name='index'), #/accounts/Behzad_test1_Path/
    re_path(r'^Behzad_test2_Path$', views.index, name='index'), #/accounts/Behzad_test2_Path
    
    
    
    re_path(r'^$', views.home, name='Home'),
    re_path(r'^about/$', views.about, name='Accounts_About'),
    re_path(r'^home/$', views.home, name='Home'),
    re_path(r'^contact/$', views.contact, name='Accounts_Contact'),
    
    re_path(r'^$', views.index, name='home'),
]

