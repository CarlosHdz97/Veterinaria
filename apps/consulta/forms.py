from django import forms
from apps.consulta.models import Consulta
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
        'servicio':'Servicio',
        }
        widgets = {
        'Fecha':forms.TextInput(),
        'Hora':forms.TextInput(),
        'Mascota':forms.TextInput(),
        'Medico':forms.TextInput(),
        'Servicio':forms.TextInput(),
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
