from .models import Activo
from .serializers import ActivoSerializer
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

class ActivoList(ListCreateAPIView):
    serializer_class = ActivoSerializer
    queryset = Activo.objects.all()
    filter_fields = ('tipo', 'fecha_compra', 'serial',)


class ActivoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ActivoSerializer
    queryset = Activo.objects.all()
