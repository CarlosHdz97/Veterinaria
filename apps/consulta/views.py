from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.consulta.forms import ConsultaForm
from apps.consulta.models import Consulta
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import time
import datetime

class ConsultaList(ListView):
    model = Consulta
    template_name = 'consulta/reporteConsulta.html'

def Consulta_list(request,id_mascota):
    hoy = time.strftime("%Y-%m-%d")
    print (hoy)
    print (hoy)
    consulta = Consulta.objects.filter(mascota = id_mascota)
    contexto = {'consultas':consulta}
    print(contexto)
    return render(request, 'consulta/reportesConsultas.html', contexto)

def Historial(request,id_mascota):

    consulta = Consulta.objects.filter(mascota = id_mascota)
    contexto = {'consultas':consulta}
    return render(request, 'consulta/reportesConsultas.html', contexto)

class ConsultaCreate(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consulta/altaConsulta.html'
    success_url = reverse_lazy('appointment:principal')

class ConsultaUpdate(UpdateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'consulta/altaConsulta.html'
    success_url = reverse_lazy('appointment:principal')

class ConsultaDelete(DeleteView):
    model = Consulta
    template_name = 'consulta/bajaConsulta.html'
    success_url = reverse_lazy('appointment:principal')
