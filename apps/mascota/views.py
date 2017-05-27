from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.mascota.models import Mascota
from apps.mascota.forms import MascotaForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/altaMascota.html'
    success_url = reverse_lazy('pet:principal')

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/reporteMascota.html'

def mascota_list(request,rfc_cliente):
    print(rfc_cliente)
    mascota = Mascota.objects.filter(cliente = rfc_cliente)
    contexto = {'mascotas':mascota}
    print(contexto)
    return render(request, 'mascota/reportesMascota.html', contexto)

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/altaMascota.html'
    success_url = reverse_lazy('pet:principal')

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/bajaMascota.html'
    success_url = reverse_lazy('pet:principal')
