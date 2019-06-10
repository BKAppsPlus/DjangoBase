from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms

#from TTL.apps.web import views
#import TTL.apps.accounts.views

from .views import *
#app_name = 'web'


service_provider_patterns = [
    re_path(r'^$',views.sp.index),
    re_path(r'^home/$',views.sp.home),

    re_path(r'^ct/$', TTL.apps.web.views.sp.PartyTypeListView.as_view(), name='clienttype-list'),
    re_path(r'^ct/(?P<pk>\d+)$', TTL.apps.web.views.sp.PartyTypeDetailView.as_view(), name='clienttype-detail'),

    re_path(r'^c/$', TTL.apps.web.views.sp.ClientListView.as_view(), name='client-list'),
    re_path(r'^c/(?P<pk>\d+)$', TTL.apps.web.views.sp.ClientDetailView.as_view(), name='client-detail'),


]
consumer_patterns = [
    re_path(r'^$',views.c.index),
]

web_patterns = [
    #re_path(r'^$',TTL.apps.web.views.web.index),
    #url(r'^(?P<store_id>\d+)/$',stores_views.detail),
    #re_path(r'^home/$', views.web.home, name='Home'),
    
    re_path(r'^$',views.web.index),
    re_path(r'^home', views.web.home, name='Home'),
    re_path(r'^about/$', views.web.about, name='Accounts_About'),
    re_path(r'^contact/$', views.web.contact, name='Accounts_Contact'),
    re_path(r'^index', views.web.index),
]

urlpatterns = [
    re_path(r'^sp/', include(service_provider_patterns)),
    re_path(r'^c/', include(consumer_patterns)),
    re_path(r'^', include(web_patterns)),
    #re_path(r'^$', include(web_patterns)),
]




