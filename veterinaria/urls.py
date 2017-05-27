"""veterinaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^home/', include('apps.home.urls', namespace = "home")),
    url(r'^customer/', include('apps.cliente.urls', namespace = "customer")),
    url(r'^appointment/', include('apps.consulta.urls', namespace = "appointment")),
    url(r'^pet/', include('apps.mascota.urls', namespace="pet")),
    url(r'^doctor/', include('apps.medico.urls', namespace = "doctor")),
    url(r'^service/', include('apps.servicio.urls', namespace = "service")),
]
