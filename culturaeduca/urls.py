from django.conf.urls import patterns, include, url
from filebrowser.sites import site
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', 'front.views.index', name='index'),
    url(r'^sobre/', 'conteudo.views.sobre', name='sobre'),
    #url(r'^mapa/', 'front.views.mapa', name='mapa'),
    url(r'^busca/', 'front.views.busca', name='busca'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^busca_escola/', 'front.views.busca_escola', name='busca'),
    url(r'^busca_mun/', 'front.views.busca_mun', name='busca_mun'),
    url(r'^dados/', 'front.views.dados', name='dados'),
    url(r'^cadastro/', 'front.views.cadastro', name='cadastro'),
    url(r'^carousel/', 'front.views.carousel', name='carousel'),

    url(r'^territorio/', include('territorio.urls')),
    url(r'^ibge/', include('ibge.urls')),
    url(r'^escola/', include('escola.urls')),
    url(r'^biblioteca/', include('biblioteca.urls')),
    url(r'^cra/', include('cra.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^mapa/', include('mapa.urls')),
    url(r'^saude/', include('saude.urls')),
    url(r'^museu/', include('museu.urls')),
    url(r'^teatro/', include('teatro.urls')),
    url(r'^cinema/', include('cinema.urls')),
    url(r'^centro_ciencia/', include('centro_ciencia.urls')),
    url(r'^sala_verde/', include('sala_verde.urls')),
    url(r'^ponto_cultura/', include('ponto_cultura.urls')),

)
