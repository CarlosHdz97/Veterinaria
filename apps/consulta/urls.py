from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.consulta.views import ConsultaList, ConsultaCreate, ConsultaUpdate, ConsultaDelete
urlpatterns = [
    url(r'^read/$',login_required(ConsultaList.as_view()), name='principal'),
    url(r'^create/$',login_required(ConsultaCreate.as_view()), name='create_appointment'),
    url(r'^update/(?P<pk>\w+)/$',login_required(ConsultaUpdate.as_view()), name='update_appointment'),
    url(r'^delete/(?P<pk>\w+)/$', login_required(ConsultaDelete.as_view()), name='delete_appointment')
]
