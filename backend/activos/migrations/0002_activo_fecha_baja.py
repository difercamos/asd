# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activo',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True),
        ),
    ]
