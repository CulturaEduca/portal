from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^kml_ponto_cultura/(?P<codigo_ibge>[-\w]+)/$', 'ponto_cultura.views.kml_ponto_cultura_municipio', name='kml_ponto_cultura'),
    url(r'^escola/(?P<codigo_inep>[-\w]+)/$', 'ponto_cultura.views.kml_ponto_cultura_escola', name='kml_ponto_cultura_escola'),
    url(r'^(?P<codigo>[-\w]+)/$', 'ponto_cultura.views.detalhes', name='ponto_cultura_detalhes'),
)