from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^kml_cras/(?P<codigo_ibge>[-\w]+)/$', 'cra.views.kml_cra_municipio', name='kml_cra'),
    url(r'^escola/(?P<codigo_inep>[-\w]+)/$', 'cra.views.kml_cra_escola', name='kml_cra_escola'),
    url(r'^(?P<codigo>[-\w]+)/$', 'cra.views.detalhes', name='cra_detalhes'),
)
