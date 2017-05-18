from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.medico.models import Medico
from apps.medico.forms import MedicoForm, MedicoUpdateForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
class MedicoCreate(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/altaMedico.html'
    success_url = reverse_lazy('doctor:principal')

class MedicoList(ListView):
    model = Medico
    template_name = 'medico/reporteMedico.html'

class MedicoUpdate(UpdateView):
    model = Medico
    form_class = MedicoUpdateForm
    template_name = 'medico/actualizacionMedico.html'
    success_url = reverse_lazy('doctor:principal')

class MedicoDelete(DeleteView):
    model = Medico
    template_name = 'medico/bajaMedico.html'
    success_url = reverse_lazy('doctor:principal')
