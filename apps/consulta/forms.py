from django import forms
from apps.consulta.models import Consulta, Factura
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta

        fields =[
        'fecha',
        'hora',
        'mascota',
        'medico',
        'servicio',
        ]
        labels = {
        'fecha':'Fecha',
        'hora':'Hora',
        'mascota':'Mascota',
        'medico':'Medico',
        'servicio':'Servicios',
        }
        widgets = {
        'fecha':forms.TextInput(),
        'hora':forms.TextInput(),
        'mascota':forms.Select(),
        'medico':forms.Select(),
        'servicio':forms.SelectMultiple(),
        }
class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura

        fields =[
        'fecha',
        'hora',
        'consulta',
        ]
        labels = {
        'fecha':'Fecha',
        'hora':'Hora',
        'consulta':'Consulta',
        }
        widgets = {
        'Fecha':forms.TextInput(),
        'Hora':forms.TextInput(),
        'Consulta':forms.TextInput(),
        }
