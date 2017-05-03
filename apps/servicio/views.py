from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.servicio.models import Servicio
from apps.servicio.forms import ServicioForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
class ServicioCreate(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicio/altaServicio.html'
    success_url = reverse_lazy('service:principal')
class ServicioList(ListView):
    model = Servicio
    template_name = 'servicio/reporteServicio.html'

class ServicioUpdate(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicio/altaservicio.html'
    success_url = reverse_lazy('service:principal')

class ServicioDelete(DeleteView):
    model = Servicio
    template_name = 'servicio/bajaServicio.html'
    success_url = reverse_lazy('service:principal')
