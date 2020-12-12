"""marcianosISI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from marcianos.models import nave_nodriza
from marcianos.models import aeronave
from marcianos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.nave_nodrizaList, name = 'naves_list'),
    path(r'navenodriza/create$', views.nave_nodriza_create, name = 'naves_create'),
    path(r'navenodriza/delete(?P<pk>\d+)$', views.nave_nodriza_delete, name ='naves_delete'),
    path('aeronave/', views.aeronaveList, name = 'aeronaves_list'),
    path(r'aeronave/create$', views.aeronave_create, name = 'aeronave_create'),
    path(r'aeronave/delete(?P<pk>\d+)$', views.aeronave_delete, name ='aeronave_delete'),
    path(r'pasajero/create$', views.pasajero_create, name='pasajero_create'),
    path(r'pasajero/list', views.pasajero_list, name='pasajero_list'),
    path(r'pasajero/delete(?P<pk>\d+)$', views.pasajero_delete, name='pasajero_delete'),
]
