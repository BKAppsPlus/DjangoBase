
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

    url(r'^$', TTL.apps.base.views.HomeView.as_view(), name='home'),
    #url(r'^$', TTL.apps.base.views.facility.index),
    #url(r'^facility$', TTL.apps.base.views.facility.index),
    #re_path('', include('django.contrib.auth.urls'))
]

