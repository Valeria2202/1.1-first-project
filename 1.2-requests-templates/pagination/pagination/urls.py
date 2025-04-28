
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_stations(request):
    return redirect('bus_stations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stations/', include('stations.urls')),
    path('', redirect_to_stations),
]