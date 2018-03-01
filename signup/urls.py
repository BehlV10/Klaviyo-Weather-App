"""Weather_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from . import views as Weather_App_views
#from Weather_App.views import index, confirm

urlpatterns = [
    #path('', Weather_App_views.index, name='index'),
    #path('confirm/', Weather_App_views.confirm, name='index'),
    url(r'^$', Weather_App_views.index, name='index'),
    url(r'confirm/$', Weather_App_views.confirm, name='confirm'),
]
"""
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
        # ex: /polls/5/
    path('<int:question_id>/', views.weather, name='weather'),
]
"""