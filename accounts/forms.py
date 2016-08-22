import datetime

from django import forms
from django.contrib.auth.models import User

from material import *

class RegistroUserForm(forms.Form):

    username = forms.CharField(min_length=2)
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(min_length=4, widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    cedula = forms.CharField(max_length=8)
    genero = forms.ChoiceField(choices=((None, ''), ('F', 'Mujer'), ('M', 'Hombre')))
    fecha_nacimiento = forms.DateField(initial=datetime.date.today)
    telefono = forms.CharField(max_length=13, initial='+58')
    direccion = forms.CharField(max_length=80)
    rol = forms.ChoiceField(choices=((None, ''), ('C', 'Cliente'), ('A', 'Administrador'), ('S', 'Superusuario')))
    #photo = forms.ImageField(required=False)

    layout = Layout('username', 'email',
                    Row('password', 'password_confirm'),
                    Fieldset('Datos Personales',
                             Row('nombre', 'apellido'),
                             Row('cedula', 'fecha_nacimiento'),
                             'genero', 'direccion',
                             Row('telefono', 'rol')))

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual en la db.')
        return email

    def clean_password_confirm(self):
        """Comprueba que password y password_confirm sean iguales."""
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError('Las contrasenas no coinciden.')
        return password_confirm

#    def clean_cedula(self):
#        """Comprueba que no exista una cedula igual en la db"""
#        cedula = self.cleaned_data['cedula']
#        if User.objects.filter(cedula=cedula):
#            raise forms.ValidationError('Cedula ya registrada.')
#        return cedula
