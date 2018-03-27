from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('Weather_App/', include('Weather_App.urls')),
    path('admin/', admin.site.urls),
]