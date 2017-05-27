from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.consulta.views import ConsultaList, ConsultaCreate
urlpatterns = [
    url(r'^read/$',login_required(ConsultaList.as_view()), name='principal'),
    url(r'^create/$',login_required(ConsultaCreate.as_view()), name='create_appointment'),
]
