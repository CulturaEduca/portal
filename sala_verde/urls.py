from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^kml_sala_verde/(?P<codigo_ibge>[-\w]+)/$', 'sala_verde.views.kml_sala_verde_municipio', name='kml_sala_verde'),
    url(r'^escola/(?P<codigo_inep>[-\w]+)/$', 'sala_verde.views.kml_sala_verde_escola', name='kml_sala_verde_escola'),
    url(r'^(?P<codigo>[-\w]+)/$', 'sala_verde.views.detalhes', name='sala_verde_detalhes'),
)