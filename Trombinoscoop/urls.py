"""Trombinoscoop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
#from Trombinoscoop.views import welcome, login, register, add_friend, show_profile, modify_profile, ajax_check_email_field, ajax_add_Friend
from Trombinoscoop import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    url('^$', views.welcome),
    url('^login$', views.login),
    url('^welcome$', views.welcome),
    url('^register$', views.register),
    url('^addFriend$', views.add_friend),
    url('^showProfile$', views.show_profile),
    url('^modifyProfile$', views.modify_profile),
    url('^Disconnect$', views.disconnect),
    url('^ajax/addFriend$', views.ajax_add_Friend),
    url('^ajax/checkEmailField$', views.ajax_check_email_field),
    url('^admin/', admin.site.urls),
]
