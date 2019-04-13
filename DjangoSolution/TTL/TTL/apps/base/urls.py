
from django.conf.urls import url, include
from django.urls import path, re_path

from TTL.apps.base import views
import TTL.apps.base.views

from . import views

app_name = 'base'

urlpatterns = [


    url(r'^$', TTL.apps.base.views.HomeView.as_view(), name='home'),
    #url(r'^addresses/$', TTL.apps.base.views.AddressesView.as_view(), name='addresses'),

    url(r'^clienttype/$', TTL.apps.base.views.ClientTypeListView.as_view(), name='clienttype_list'),
    url(r'^clienttype/add/$', TTL.apps.base.views.ClientTypeCreateView.as_view(), name='clienttype-add'),
    url(r'^clienttype-(?P<pk>\d+)$', TTL.apps.base.views.ClientTypeDetailView.as_view(), name='clienttype-detail'),
    url(r'^clienttype/(?P<pk>\d+)$', TTL.apps.base.views.ClientTypeUpdateView.as_view(), name='clienttype-update'),
    
    url(r'^client/$', TTL.apps.base.views.ClientListView.as_view(), name='client-list'),
    url(r'^client/add/$', TTL.apps.base.views.ClientCreateView.as_view(), name='client-add'),
    url(r'^client-(?P<pk>\d+)$', TTL.apps.base.views.ClientDetailView.as_view(), name='client-detail'),
    url(r'^client/(?P<pk>\d+)$', TTL.apps.base.views.ClientUpdateView.as_view(), name='client-update'),
    
    url(r'^address/$', TTL.apps.base.views.AddressListView.as_view(), name='address-list'),
    url(r'^address/add/$', TTL.apps.base.views.AddressCreateView.as_view(), name='address-add'),
    url(r'^address/(?P<pk>\d+)$', TTL.apps.base.views.AddressDetailView.as_view(), name='address-detail'),

    url(r'^mystuff/$', TTL.apps.base.views.MyStuff.as_view(), name='mystuff'),
    url(r'^allstuff/$', TTL.apps.base.views.AllStuff.as_view(), name='allstuff'),


]

