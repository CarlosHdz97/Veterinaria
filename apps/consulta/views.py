from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.consulta.forms import ConsultaForm
from apps.consulta.models import Consulta
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.

class ConsultaList(ListView):
    model = Consulta
    template_name = 'consulta/reporteConsulta.html'

class ConsultaCreate(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consulta/altaConsulta.html'
    success_url = reverse_lazy('appointment:principal')
