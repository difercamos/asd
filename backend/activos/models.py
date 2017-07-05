# -*- coding: UTF-8 -*-
from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Activo(models.Model):
    estado_choices = (
        ('A', 'Activo'),
        ('B', 'Dado De Baja'),
        ('R', 'En Reparacion'),
        ('D', 'Disponible'),
        ('AS', 'Asignado'),
    )

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=50)
    serial = models.CharField(max_length=30)
    numero_interno = models.CharField(max_length=20)
    peso = models.FloatField(blank=True, null=True)
    alto = models.FloatField(blank=True, null=True)
    ancho = models.FloatField(blank=True, null=True)
    largo = models.FloatField(blank=True, null=True)
    valor_compra = models.FloatField()
    fecha_compra = models.DateField()
    fecha_baja = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=estado_choices)
    color = models.CharField(max_length=50, blank=True, null=True)
    ubicacion = models.PointField(blank=True, null=True)
    usuario = models.ForeignKey(User, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.fecha_baja is None:
            if self.fecha_baja > self.fecha_compra:
                super(Activo, self).save(*args, **kwargs)
            else:
                print("error")
        else:
            super(Activo, self).save(*args, **kwargs)
