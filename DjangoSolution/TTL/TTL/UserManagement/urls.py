from django.conf.urls import url, include
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms

from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetForm
from django.contrib.auth.views import PasswordResetView


from . import views

app_name = 'UserManagement'

urlpatterns = [
    re_path(r'^Behzad_test0_Path', views.index, name='index'), #/UserManagement/Behzad_test0_PathABCDEFGHI
    re_path(r'^Behzad_test1_Path/$', views.index, name='index'), #/UserManagement/Behzad_test1_Path/
    re_path(r'^Behzad_test2_Path$', views.index, name='index'), #/UserManagement/Behzad_test2_Path
    
    
    
    re_path(r'^$', views.home, name='Accounts_Home'),
    re_path(r'^about$', views.about, name='Accounts_About'),
    re_path(r'^home$', views.home, name='Accounts_Home'),
    re_path(r'^contact$', views.contact, name='Accounts_Contact'),
    
    re_path(r'^$', views.index, name='home'),
    
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='UserManagement/login.html'),name='Accounts_Login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='UserManagement/loggedoff.html'),name='Accounts_Loggedoff'),
    re_path(r'^register/$', views.register, name='Accounts_Register'),
    re_path(r'^profile/$', views.profile_view, name='Accounts_ViewProfile'),
    re_path(r'^profile/edit/$', views.profile_edit, name='Accounts_EditProfile'),
    re_path(r'^profile/change-password/$', views.change_password, name='Accounts_ChangePassword'),
    re_path(r'^password-reset/$', auth_views.PasswordResetView.as_view(),name='Accounts_ResetPassword'),

    #re_path('', include('django.contrib.auth.urls'))
]

