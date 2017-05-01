from django.db import models
from apps.mascota.models import Mascota
from apps.medico.models import Medico
from apps.servicio.models import Servicio
# Create your models here.
class Consulta(models.Model):
    fecha = models.DateField()
    hora = models.CharField(max_length=20)
    mascota = models.ForeignKey(Mascota, null = True, blank = True, on_delete = models.CASCADE,)
    medico = models.ForeignKey(Medico, null = True, blank = True, on_delete = models.CASCADE,)
    servicio = models.ManyToManyField(Servicio)
    def __str__(self):
        return '{}'.format(self.mascota)

class Factura(models.Model):
    fecha = models.DateField()
    hora = models.CharField(max_length=20)
    consulta = models.OneToOneField(Consulta, null = True, blank = True, on_delete = models.CASCADE,)
    def __str__(self):
        return '{}'.format(self.id)
class Historial(models.Model):
    consulta = models.ForeignKey(Consulta, null = True, blank = True, on_delete = models.CASCADE,)
    fechaSeguimiento = models.DateField()
    hora = models.CharField(max_length=20)
    mascota = models.ForeignKey(Mascota, null = True, blank = True, on_delete = models.CASCADE,)
    def __str__(self):
        return '{}'.format(self.mascota)
