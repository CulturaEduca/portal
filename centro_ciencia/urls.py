from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^kml_centro_ciencia/(?P<codigo_ibge>[-\w]+)/$', 'centro_ciencia.views.kml_centro_ciencia_municipio', name='kml_centro_ciencia'),
    url(r'^escola/(?P<codigo_inep>[-\w]+)/$', 'centro_ciencia.views.kml_centro_ciencia_escola', name='kml_centro_ciencia_escola'),
    url(r'^(?P<codigo>[-\w]+)/$', 'centro_ciencia.views.detalhes', name='centro_ciencia_detalhes'),
)