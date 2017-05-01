from django.db import models

# Create your models here.
class Servicio(models.Model):
    descripcion = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    tipo = models.CharField(max_length=25)
    periodicidad = models.CharField(max_length=12)
    def __str__(self):
        return '{}'.format(self.id)
