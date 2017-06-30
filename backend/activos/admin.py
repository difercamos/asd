from django.contrib import admin

from .models import Activo

import floppyforms.__future__ as forms


class GmapPointWidget(forms.gis.BaseGMapWidget,
                      forms.gis.PointWidget):
    map_width = 800
    map_height = 600
    template_name = 'google_maps.html'
    google_maps_api_key = 'AIzaSyCohCKYdJOHyCyBdXlBfFG7sLNjqpiJSnE'


class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        exclude = ()
        widgets = {
            'ubicacion': GmapPointWidget
        }


@admin.register(Activo)
class ActivoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'tipo',
        'serial',
        'numero_interno'
    )
    search_fields = (
        'nombre',
        'tipo',
        'serial',
        'numero_interno'
    )
    form = ActivoForm
