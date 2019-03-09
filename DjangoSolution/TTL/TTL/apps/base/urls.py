
from django.conf.urls import url, include
from django.urls import path, re_path

from TTL.apps.base import views
import TTL.apps.base.views

from . import views

app_name = 'base'

urlpatterns = [
    re_path(r'^Behzad_test0_Path', views.index, name='index'), #/user/Behzad_test0_PathABCDEFGHI
    re_path(r'^Behzad_test1_Path/$', views.index, name='index'), #/user/Behzad_test1_Path/
    re_path(r'^Behzad_test2_Path$', views.index, name='index'), #/user/Behzad_test2_Path

    url(r'^$', TTL.apps.base.views.AddressesView.as_view(), name='home'),
    url(r'^addresses/$', TTL.apps.base.views.AddressesView.as_view(), name='addresses'),

    url(r'^address/$', TTL.apps.base.views.AddressIndexView.as_view(), name='address-list'),
    url(r'^address/(?P<pk>\d+)$', TTL.apps.base.views.AddressDetailView.as_view(), name='address-detail'),
    url(r'^address/add/$', TTL.apps.base.views.AddressCreateView0.as_view(), name='address-add'),
    

    #url(r'^address/$', TTL.apps.base.views.AddressesView.as_view(), name='address-add'),
    #url(r'^address/(?P<pk>\d+)$', TTL.apps.base.views.AddressView.as_view(), name='address-update'),
    #url(r'^address/(?P<pk>\d+)/delete/$', TTL.apps.base.views.AddressesView.as_view(), name='address-delete'),

    #url(r'^address/(?P<pk>\d+)$', TTL.apps.base.views.AddressesView.as_view(), name='base_address'),
    
    #url(r'^$', TTL.apps.base.views.facility.index),
    #url(r'^facility$', TTL.apps.base.views.facility.index),
    #re_path('', include('django.contrib.auth.urls'))
]

