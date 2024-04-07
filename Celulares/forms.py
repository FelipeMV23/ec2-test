from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Celulares.models import Celular
from django.core import validators
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='',  # Eliminar la etiqueta visual
        widget=forms.EmailInput(attrs={'placeholder': 'Correo Electrónico', 'class': 'controls'}),
        required=True
    )
    username = forms.CharField(
        label='',  # Eliminar la etiqueta visual
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de Usuario', 'class': 'controls'}),
        required=True
    )
    password1 = forms.CharField(
        label='',  # Eliminar la etiqueta visual
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'controls'}),
        required=True
    )
    password2 = forms.CharField(
        label='',  # Eliminar la etiqueta visual
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmación de Contraseña', 'class': 'controls'}),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def clean_username(self):
        username = self.cleaned_data['username']

        if len(username) < 3:
            raise ValidationError('el nombre de es demasiado corto...')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        
        if len(password1 and password2) < 8:
            raise ValidationError("La contraseña es demasiado corta.")
        
        if len(password1 and password2) < 8:
            raise ValidationError("La contraseña es demasiado corta.")
        
        return password2

          
class FormCelular(forms.ModelForm):
    class Meta:
        model = Celular
        fields = ['nombre', 'quantity', 'marca', 'foto', 'descripcion', 'precio',]
        labels = {
            'nombre': 'Nombre',
            'quantity': 'Cantidad',
            'marca' : 'Marca',
            'foto': 'Foto',
            'descripcion': 'Descripción',
            'precio' : 'Precio',
        }



