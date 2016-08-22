from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from datetime import datetime
from django.core.validators import RegexValidator

# Create your models here.
class UserProfile(models.Model):

    GENEROS = (
                (None, ''),
                ('F', 'Mujer'),
                ('M', 'Hombre'),
            )

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    email = models.EmailField(default='')
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    cedula = models.CharField(max_length=8, default='')
    genero = models.CharField(max_length=1, choices=GENEROS, default=None)
    fecha_nacimiento = models.DateTimeField(default=datetime.now)
    telefono = models.CharField(max_length=13, default='+58')
    direccion = models.CharField(max_length=80, default='Valencia, Venezuela')

    #photo = models.ImageField(upload_to='profiles', blank=True, null=True)

    def __str__(self):
        return self.user.username


class UserRole(models.Model):

    ROLE_CHOICES = (
        (None, ''),
        ('C', 'Cliente'),
        ('A', 'Administrador'),
        ('S', 'Superusuario'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    rol = models.CharField(max_length=1, choices=ROLE_CHOICES, default=None)

    def __str__(self):
        return self.user
