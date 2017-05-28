from django.db import models

# Create your models here.
class Medico(models.Model):
    rfc = models.CharField(max_length=16, primary_key=True)
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    def __str__(self):
        return '{}'.format(self.nombre)
