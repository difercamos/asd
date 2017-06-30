from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^activos/$', views.ActivoList.as_view(), name='activo-list'),
    url(r'^activos/(?P<pk>[0-9]+)/$', views.ActivoDetail.as_view(), name='activo-detail'),
]
