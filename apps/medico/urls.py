from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.medico.views import MedicoCreate, MedicoList, MedicoUpdate,MedicoDelete
urlpatterns = [
    url(r'^create/$',login_required(MedicoCreate.as_view()), name='create_doctor'),
    url(r'^read/$',login_required(MedicoList.as_view()), name='principal'),
    url(r'^update/(?P<pk>\w+)/$',login_required(MedicoUpdate.as_view()), name='update_doctor'),
    url(r'^delete/(?P<pk>\w+)/$', login_required(MedicoDelete.as_view()), name='delete_doctor'),
    ]
