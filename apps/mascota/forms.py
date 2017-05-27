from django import forms
from apps.mascota.models import Mascota
class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota

        fields =[
        'nombre',
        'especie',
        'raza',
        'color',
        'tamano',
        'senaParticular',
        'fechaNacimiento',
        'cliente',
        ]
        labels = {
        'nombre':'Nombre',
        'especie':'Especie',
        'raza':'Raza',
        'color':'Color',
        'tamano':'Tamaño',
        'senaParticular':'Seña Particular',
        'fechaNacimiento' :'Fecha de Nacimiento',
        'cliente':'Cliente',
        }
        widgets = {
        'nombre':forms.TextInput(),
        'especie':forms.TextInput(),
        'raza':forms.TextInput(),
        'color':forms.TextInput(),
        'tamano':forms.TextInput(),
        'senaParticular':forms.TextInput(),
        'fechaNacimiento':forms.DateInput(),
        'cliente':forms.TextInput(),
        }
