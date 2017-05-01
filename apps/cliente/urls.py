from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.cliente.views import ClienteCreate, ClienteList, ClienteUpdate,ClienteDelete
urlpatterns = [
    url(r'^create/$',login_required(ClienteCreate.as_view()), name='create_customer'),
    url(r'^read/$',login_required(ClienteList.as_view()), name='principal'),
    url(r'^update/(?P<pk>\w+)/$',login_required(ClienteUpdate.as_view()), name='update_customer'),
    url(r'^delete/(?P<pk>\w+)/$', login_required(ClienteDelete.as_view()), name='delete_customer'),
]
