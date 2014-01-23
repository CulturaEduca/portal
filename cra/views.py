# -*- coding: utf-8 -*-

from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

icone = '/static/mapa/cra.png'

def detalhes(request, codigo):
    '''Tela de detalhe dos CRAS'''

    from cra.models import Cra

    cra = Cra.objects.get(id = int(codigo))

    longitude = str(cra.geom.x).replace(',','.')
    latitude = str(cra.geom.y).replace(',','.')

    return render_to_response('cras/detalhes.html', {
        'cra': cra,
        'icone': icone,
        'latitude': latitude,
        'longitude': longitude,
        'nome_ponto': 'CRA'
        })

def kml_cra_municipio(request, codigo_ibge):
    '''Lista em KML todas as escolas de um municipio'''

    from cra.models import Cra
    from ibge.models import Municipio
    import simplekml

    mun = Municipio.objects.get(cd_geocodm = int(codigo_ibge))

    poi = Cra.objects.filter(geom__intersects = mun.area)

    kml = simplekml.Kml()

    for e in poi:
        pnt = kml.newpoint(
            name = unicode(e.nome),
            description = '/cra/' + str(e.id),
            coords = [(e.geom.x, e.geom.y)]
            )
        pnt.style.iconstyle.scale = 1
        pnt.style.iconstyle.icon.href = icone

    return HttpResponse(kml.kml(), mimetype='Content-Type:application/vnd.google-earth.kml+xml')


def kml_cra_escola(request, codigo_inep):
    '''POI com base na escola'''

    from django.contrib.gis.measure import Distance, D
    from cra.models import Cra
    from escola.models import Escola
    from django.contrib.gis.geos import Point, Polygon, MultiPolygon
    import simplekml

    distancia = Distance(km = 1)

    escola = Escola.objects.get(codigo_inep = codigo_inep)

    ll = escola.latlong

    poi = Cra.objects.filter(geom__distance_lt = (ll, distancia))

    kml = simplekml.Kml()

    for x in poi:
        pnt = kml.newpoint(
            name = unicode('oi'),
            description = 'oi',
            coords = [(x.geom.x, x.geom.y)])
        pnt.style.iconstyle.scale = 1
        pnt.style.iconstyle.icon.href = icone


    return HttpResponse(kml.kml(), mimetype='Content-Type:application/vnd.google-earth.kml+xml')
