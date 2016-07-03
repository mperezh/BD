from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class Usuarios(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photho = models.ImageField(upload_to='profiles', blank=True, null=True)