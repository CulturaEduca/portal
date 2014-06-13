# -*- coding: utf-8 -*-

from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

icone = '/static/mapa/book.png'


def kml_biblioteca_municipio(request, codigo_ibge):
    '''Lista em KML todas as escolas de um municipio'''

    from biblioteca.models import Biblioteca
    from ibge.models import Municipio
    import simplekml

    mun = Municipio.objects.get(cd_geocodm=int(codigo_ibge))

    bb = Biblioteca.objects.filter(geom__intersects=mun.area)

    kml = simplekml.Kml()

    for e in bb:
        pnt = kml.newpoint(
            name=unicode(e.nome),
            description='/biblioteca/' + str(e.id),
            coords=[(e.geom.x, e.geom.y)]
        )
        pnt.style.iconstyle.scale = 1
        pnt.style.iconstyle.icon.href = icone

    return HttpResponse(kml.kml(), mimetype='Content-Type:application/vnd.google-earth.kml+xml')


def kml_biblioteca_escola(request, codigo_inep):
    '''POI com base na escola'''

    from django.contrib.gis.measure import Distance, D
    from biblioteca.models import Biblioteca
    from escola.models import Escola
    from django.contrib.gis.geos import Point, Polygon, MultiPolygon
    import simplekml

    distancia = Distance(km=1)

    escola = Escola.objects.get(codigo_inep=codigo_inep)

    ll = escola.latlong

    biblios = Biblioteca.objects.filter(geom__distance_lt=(ll, distancia))

    kml = simplekml.Kml()

    for x in biblios:
        pnt = kml.newpoint(
            name=unicode(x.nome),
            description='/biblioteca/' + str(x.id),
            coords=[(x.geom.x, x.geom.y)])
        pnt.style.iconstyle.scale = 1
        pnt.style.iconstyle.icon.href = icone


    return HttpResponse(kml.kml(), mimetype='Content-Type:application/vnd.google-earth.kml+xml')

def detalhes(request, codigo):
    '''Tela de detalhe das Bibliotecas'''

    from biblioteca.models import Biblioteca
    from sniic.models import Tipologia

    biblioteca = Biblioteca.objects.get(id = int(codigo))

    s1 = biblioteca.sniic_n1
    if not '.' in s1:
        s1 = s1 + '.'
    s2 = biblioteca.sniic_n2
    s3 = biblioteca.sniic_n3

    try:
        sniic1 = Tipologia.objects.get(codigo = s1)
    except:
        sniic1 = False
    try:
        sniic2 = Tipologia.objects.get(codigo = s2)
    except:
        sniic2 = False
    try:
        sniic3 = Tipologia.objects.get(codigo = s3)
    except:
        sniic3 = False


    longitude = str(biblioteca.geom.x).replace(',','.')
    latitude = str(biblioteca.geom.y).replace(',','.')

    return render_to_response('biblioteca/detalhes.html', {
        'biblioteca': biblioteca,
        'icone': icone,
        'latitude': latitude,
        'longitude': longitude,
        'nome_ponto': 'Biblioteca', 
        'sniic1': sniic1,
        'sniic2': sniic2,
        'sniic3': sniic3,
        })
