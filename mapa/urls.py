from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/?$', 'front.views.mapa', name='mapa'),
    url(r'^(?P<uf>[-\w]+)/$', 'mapa.views.uf', name='mapa_uf'),
    url(r'^(?P<uf>[-\w]+)/(?P<municipio>[-\w]+)/$', 'mapa.views.municipio', name='mapa_municipio'),
)
