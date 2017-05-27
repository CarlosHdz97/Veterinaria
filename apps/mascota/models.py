from django.db import models
from apps.cliente.models import Cliente
# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=25)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    tamano = models.CharField(max_length=20)
    senaParticular = models.CharField(max_length=20)
    fechaNacimiento = models.DateField()
    cliente = models.ForeignKey(Cliente, null = True, blank = True, on_delete = models.CASCADE,)
    def __str__(self):
        return '{} {}'.format(self.nombre, self.cliente)
