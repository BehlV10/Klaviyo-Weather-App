from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views as Weather_App_views

urlpatterns = [
    url(r'^$', Weather_App_views.index, name='index'),
    url(r'confirm/$', Weather_App_views.confirm, name='confirm'),
]