from django.contrib import admin
# Register your models here.
from .models import Consulta, Factura, Historial
admin.site.register(Consulta)
admin.site.register(Factura)
admin.site.register(Historial)
