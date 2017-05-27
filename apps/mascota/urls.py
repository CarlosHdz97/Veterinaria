from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.mascota.views import MascotaCreate, MascotaList, MascotaUpdate, MascotaDelete, mascota_list
urlpatterns = [
    url(r'^create/$',login_required(MascotaCreate.as_view()), name='create_pet'),
    url(r'^read/$',login_required(MascotaList.as_view()), name='principal'),
    url(r'^update/(?P<pk>\d+)/$',login_required(MascotaUpdate.as_view()), name='update_pet'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='delete_pet'),
    url(r'^reporte/(\w+)/$', mascota_list, name='reporte_mascota'),

]
