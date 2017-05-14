from django import forms
from apps.servicio.models import Servicio
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio

        fields =[
        'descripcion',
        'precio',
        'tipo',
        'periodicidad',
        ]
        labels = {
        'descripcion':'Servicio',
        'precio':'Precio',
        'tipo':'Tipo',
        'periodicidad':'Periodicidad',
        }
        widgets = {
        'descripcion': forms.TextInput(),
        'precio': forms.NumberInput(),
        'tipo': forms.TextInput(),
        'periodicidad': forms.TextInput(),
        }
