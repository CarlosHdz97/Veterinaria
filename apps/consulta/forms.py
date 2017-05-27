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
        ]
        labels = {
        'fecha':'Fecha',
        'hora':'Hora',
        'mascota':'Mascota',
        'medico':'Medico',
        }
        widgets = {
        'Fecha':forms.TextInput(),
        'Hora':forms.TextInput(),
        'Mascota':forms.TextInput(),
        'Medico':forms.Select(),
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
