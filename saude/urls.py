from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^kml_saude/(?P<codigo_ibge>[-\w]+)/$', 'saude.views.kml_saude_municipio', name='kml_saude'),
    url(r'^escola/(?P<codigo_inep>[-\w]+)/$', 'saude.views.kml_saude_escola', name='kml_saude_escola'),
    url(r'^(?P<codigo>[-\w]+)/$', 'saude.views.detalhes', name='saude_detalhes'),
)