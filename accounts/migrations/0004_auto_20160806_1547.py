# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160804_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cedula',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='direccion',
            field=models.CharField(default='Valencia, Venezuela', max_length=80),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='telefono',
            field=models.CharField(default='+58', max_length=12),
        ),
    ]