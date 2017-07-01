from rest_framework import serializers
from .models import Activo


class ActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activo
        fields = (
            'id',
            'nombre',
            'descripcion',
            'tipo',
            'serial',
            'numero_interno',
            'peso',
            'alto',
            'ancho',
            'largo',
            'valor_compra',
            'fecha_compra',
            'estado',
            'color',
            'ubicacion',
            'usuario',
        )
