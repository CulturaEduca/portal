from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^kml_museu/(?P<codigo_ibge>[-\w]+)/$', 'museu.views.kml_museu_municipio', name='kml_museu'),
    url(r'^escola/(?P<codigo_inep>[-\w]+)/$', 'museu.views.kml_museu_escola', name='kml_museu_escola'),
    url(r'^(?P<codigo>[-\w]+)/$', 'museu.views.detalhes', name='museu_detalhes'),
)