
from django.conf.urls import url, include
from django.urls import path, re_path

#from TTL.apps.base import views
#import TTL.apps.base.views

#from . import views
from .views import *
#app_name = 'base'

#re_path(r'^app_core/', include('app_core.urls')),



urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    #url(r'^addresses/$', AddressesView.as_view(), name='addresses'),

    re_path(r'^clienttype/$', ClientTypeListView.as_view(), name='clienttype-list'),
    re_path(r'^clienttype/add/$', ClientTypeCreateView.as_view(), name='clienttype-add'),
    re_path(r'^clienttype-(?P<pk>\d+)$', ClientTypeDetailView.as_view(), name='clienttype-detail'),
    re_path(r'^clienttype/(?P<pk>\d+)$', ClientTypeUpdateView.as_view(), name='clienttype-update'),
    
    re_path(r'^client/$', ClientListView.as_view(), name='client-list'),
    re_path(r'^client/add/$', ClientCreateView.as_view(), name='client-add'),
    #url(r'^client/my$', CurrClientDetailView.as_view(), name='curr-client-detail'),
    re_path(r'^client/(?P<pk>\d+)$', ClientDetailView.as_view(), name='client-detail'),
    re_path(r'^client/edit/(?P<pk>\d+)$', ClientUpdateView.as_view(), name='client-update'),
    
    re_path(r'^address/$', AddressListView.as_view(), name='address-list'),
    re_path(r'^address/add/$', AddressCreateView.as_view(), name='address-add'),
    re_path(r'^address/(?P<pk>\d+)$', AddressDetailView.as_view(), name='address-detail'),

    re_path(r'^mystuff/$', MyStuff.as_view(), name='mystuff'),
    re_path(r'^allstuff/$', AllStuff.as_view(), name='allstuff'),


]
