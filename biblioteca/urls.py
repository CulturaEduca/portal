from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^kml_bibliotecas/(?P<codigo_ibge>[-\w]+)/$', 'biblioteca.views.kml_biblioteca_municipio', name='kml_bibliotecas'),
    url(r'^escola/(?P<codigo_inep>[-\w]+)/$', 'biblioteca.views.kml_biblioteca_escola', name='kml_bibliotecas_escola'),
    url(r'^(?P<codigo>[-\w]+)/$', 'biblioteca.views.detalhes', name='biblioteca_detalhes'),
)