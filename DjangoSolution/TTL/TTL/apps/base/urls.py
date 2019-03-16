
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

    url(r'^clienttype/$', TTL.apps.base.views.ClientTypeListView.as_view(), name='clienttype_list'),
    url(r'^clienttype/add/$', TTL.apps.base.views.ClientTypeCreateView.as_view(), name='clienttype-add'),
    url(r'^clienttype/(?P<pk>\d+)$', TTL.apps.base.views.ClientTypeDetailView.as_view(), name='clienttype-detail'),
    
    url(r'^client/$', TTL.apps.base.views.ClientListView.as_view(), name='client-list'),
    url(r'^client/add/$', TTL.apps.base.views.ClientCreateView.as_view(), name='client-add'),
    url(r'^client/(?P<pk>\d+)$', TTL.apps.base.views.ClientDetailView.as_view(), name='client-detail'),
    
    url(r'^address/$', TTL.apps.base.views.AddressIndexView.as_view(), name='address-list'),
    url(r'^address/add/$', TTL.apps.base.views.AddressCreateView0.as_view(), name='address-add'),
    url(r'^address/(?P<pk>\d+)$', TTL.apps.base.views.AddressDetailView.as_view(), name='address-detail'),




    #url(r'^address/$', TTL.apps.base.views.AddressesView.as_view(), name='address-add'),
    #url(r'^address/(?P<pk>\d+)$', TTL.apps.base.views.AddressView.as_view(), name='address-update'),
    #url(r'^address/(?P<pk>\d+)/delete/$', TTL.apps.base.views.AddressesView.as_view(), name='address-delete'),

    #url(r'^address/(?P<pk>\d+)$', TTL.apps.base.views.AddressesView.as_view(), name='base_address'),
    
    #url(r'^$', TTL.apps.base.views.facility.index),
    #url(r'^facility$', TTL.apps.base.views.facility.index),
    #re_path('', include('django.contrib.auth.urls'))

    #url(r'^create/$', TTL.apps.base.views.BookCreateView.as_view(), name='create_book'),
    #url(r'^update/(?P<pk>\d+)/$', TTL.apps.base.views.BookUpdateView.as_view(), name='update_book'),
    #url(r'^books/$', TTL.apps.base.views.BookListView.as_view(), name='book_list'),
   
    #url(r'^createnew/$', TTL.apps.base.views.BooknewCreateView.as_view(), name='createnew_book'),
    #url(r'^updatenew/(?P<pk>\d+)/$', TTL.apps.base.views.BooknewUpdateView.as_view(), name='updatenew_book'),
    #url(r'^booksnew/$', TTL.apps.base.views.BooknewListView.as_view(), name='booknew_list'),
]

