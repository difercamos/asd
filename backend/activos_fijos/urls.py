from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from . import views

schema_view = get_swagger_view(title='Activos API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/$', views.api_root),
    url(r'^api/v1/', include('activos.urls', namespace='activos')),
]
