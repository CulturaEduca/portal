from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^kml_teatro/(?P<codigo_ibge>[-\w]+)/$', 'teatro.views.kml_teatro_municipio', name='kml_teatro'),
    url(r'^territorio/(?P<codigo_inep>[-\w]+)/$', 'teatro.views.kml_territorio', name='kml_teatro_territorio'),
    url(r'^(?P<codigo>[-\w]+)/$', 'teatro.views.detalhes', name='teatro_detalhes'),
)