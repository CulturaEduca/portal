from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^kml_cinema/(?P<codigo_ibge>[-\w]+)/$', 'cinema.views.kml_cinema_municipio', name='kml_cinema'),
    url(r'^escola/(?P<codigo_inep>[-\w]+)/$', 'cinema.views.kml_cinema_escola', name='kml_cinema_escola'),
    url(r'^(?P<codigo>[-\w]+)/$', 'cinema.views.detalhes', name='cinema_detalhes'),
)