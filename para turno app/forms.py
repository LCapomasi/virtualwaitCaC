from django import forms
from .models import Turno

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = [
            'nombre', 
            'apellido', 
            'edad', 
            'dni', 
            'sexo', 
            'email', 
            'operacion', 
            'fecha', 
            'motivo', 
            'terminos'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'formulario__input'}),
            'apellido': forms.TextInput(attrs={'class': 'formulario__input'}),
            'edad': forms.NumberInput(attrs={'class': 'formulario__input'}),
            'dni': forms.TextInput(attrs={'class': 'formulario__input'}),
            'sexo': forms.RadioSelect(),
            'email': forms.EmailInput(attrs={'class': 'formulario__input', 'placeholder': 'email@email.com'}),
            'operacion': forms.Select(attrs={'class': 'formulario__input'}),
            'fecha': forms.DateInput(attrs={'class': 'formulario__input'}),
            'motivo': forms.Textarea(attrs={'class': 'formulario__input', 'placeholder': 'Explique brevemente'}),
            'terminos': forms.CheckboxInput(attrs={'class': 'formulario__checkbox'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'dni': 'DNI',
            'sexo': 'Sexo',
            'email': 'Email',
            'operacion': 'Operación',
            'fecha': 'Fecha',
            'motivo': 'Motivo',
            'terminos': 'Acepto los Términos y Condiciones',
        }
