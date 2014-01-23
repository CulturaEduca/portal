from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<codigo_inep>[-\w]+)/$', 'territorio.views.detalhe', name='territorio_detalhe'),
    url(r'^ol/(?P<codigo_ibge>[-\w]+)/$', 'territorio.views.ol', name='ol'),
    url(r'^geojson/(?P<codigo_inep>[-\w]+)/$', 'territorio.views.geojson', name='territorio_geojson'),
)