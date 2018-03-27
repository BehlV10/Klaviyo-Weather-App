from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import urlimport signup.urls
import signup.views as views

app_name = "Weather_App"
urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^subscribe/', include('signup.urls'), name='signup'),
]