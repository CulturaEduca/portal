from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^contorno_municipio/(?P<ibge>[-\w]+)/$', 'ibge.views.contorno_municipio', name='contorno_municipio'),
    url(r'^centro_municipio/(?P<ibge>[-\w]+)/$', 'ibge.views.centro_municipio', name='centro_municipio'),
)