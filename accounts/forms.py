from django import forms
from django.contrib.auth.models import User

class RegistroUserForm(forms.Form):
    
    username = forms.CharField(min_length=2)
    email = forms.EmailField()
    password = forms.CharField(min_length=4, widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    #photo = forms.ImageField(required=False)
    
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