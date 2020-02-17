from django import forms
from .models import empleado, bovino, produccion, empleado_login

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = empleado
        fields = '__all__'

        widgets = {
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer Nombre'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo Nombre'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primer Apellido'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segundo Apellido'}),
            'cedula': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cedula'}),
            'celular': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Celular'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de Nacimiento', 'type': 'date'}),
            'fecha_contratacion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de Contratacion', 'type': 'date'}),
            'sueldo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Sueldo'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}),
            'id_cargo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Cargo'}),
        }

class BovinoForm(forms.ModelForm):
    class Meta:
        model = bovino
        fields = '__all__'
        
        widgets = {
            'codigo_bovino': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Codigo Bovino'}),
            'identidad_ica': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Identidad ICA'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Bovino'}),
            'nombre_madre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Madre Bovino'}),
            'nombre_padre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Padre Bovino'}),
            'cantidad_partos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad Partos'}),
            'fecha_ultimo_parto': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Ultimo Parto', 'type': 'date'}),
            'dias_lactancia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dias Lactancia'}),
            'id_tipo_bovino': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tipo Bovino'}),
        } 
    
class ProduccionForm(forms.ModelForm):
    class Meta:
        model = produccion
        fields = '__all__'
        
        widgets = {
            'id_produccion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Id Produccion'}),
            'codigo_produccion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Codigo Produccion'}),
            'fecha_produccion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Produccion', 'type': 'date'}),
            'primera_produccion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Primera Produccion (Lt)'}),
            'segunda_produccion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Segunda Produccion (Lt)'}),
            'cantidad_concentrado': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad Concentrado (Gr)'}),
            'id_empleado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Empleado'}),
            'id_bovino': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Bovino'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Observaciones'}),
        }
        
class EmpleadoLoginForm(forms.ModelForm):
    class Meta:
        model = empleado_login
        fields = '__all__'
        
        widgets = {
            'cedula': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cedula'}),            
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'clave': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Clave'}),
        }                        
