from django import forms
from apps.medico.models import Medico
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico

        fields =[
        'rfc',
        'nombre',
        'domicilio',
        'telefono',
        'email',
        ]
        labels = {
        'rfc' : 'RFC',
        'nombre' : 'Nombre',
        'domicilio':'Domicilio',
        'telefono':'Telefono',
        'email':'Email',
        }
        widgets = {
        'rfc': forms.TextInput(),
        'nombre': forms.TextInput(),
        'domicilio': forms.TextInput(),
        'telefono': forms.TextInput(),
        'email': forms.EmailInput(),
        }

class MedicoUpdateForm(forms.ModelForm):
    class Meta:
        model = Medico

        fields =[
        'nombre',
        'domicilio',
        'telefono',
        'email',
        ]
        labels = {
        'nombre' : 'Nombre',
        'domicilio':'Domicilio',
        'telefono':'Telefono',
        'email':'Email',
        }
        widgets = {
        'nombre': forms.TextInput(),
        'domicilio': forms.TextInput(),
        'telefono': forms.TextInput(),
        'email': forms.EmailInput(),
        }
