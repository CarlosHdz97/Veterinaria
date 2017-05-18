from django import forms
from apps.cliente.models import Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

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
class ClienteUpdateForm(forms.ModelForm):
    class Meta:
        model = Cliente

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
