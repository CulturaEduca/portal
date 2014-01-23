from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^geojson/(?P<ibge>[-\w]+)/$', 'escola.views.geojson_escolas', name='geojson_escolas'),
    url(r'^kml/(?P<codigo_inep>[-\w]+)/$', 'escola.views.kml_escola', name='kml_escola'),
    url(r'^kml_escolas/(?P<codigo_ibge>[-\w]+)/$', 'escola.views.kml_escolas_municipio', name='kml_escolas'),
)