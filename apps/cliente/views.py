from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.cliente.models import Cliente
from apps.cliente.forms import ClienteForm, ClienteUpdateForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/altaCliente.html'
    success_url = reverse_lazy('pet:create_pet')

class ClienteList(ListView):
    model = Cliente
    template_name = 'cliente/reporteCliente.html'

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteUpdateForm
    template_name = 'cliente/actualizacionCliente.html'
    success_url = reverse_lazy('customer:principal')

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cliente/bajaCliente.html'
    success_url = reverse_lazy('customer:principal')
