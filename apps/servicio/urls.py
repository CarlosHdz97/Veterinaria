from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.servicio.views import ServicioCreate, ServicioList, ServicioUpdate,ServicioDelete
urlpatterns = [
    url(r'^create/$',login_required(ServicioCreate.as_view()), name='create_service'),
    url(r'^read/$',login_required(ServicioList.as_view()), name='principal'),
    url(r'^update/(?P<pk>\w+)/$',login_required(ServicioUpdate.as_view()), name='update_service'),
    url(r'^delete/(?P<pk>\w+)/$', login_required(ServicioDelete.as_view()), name='delete_service'),
]
