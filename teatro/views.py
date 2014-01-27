# -*- coding: utf-8 -*-

from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

icone = '/static/mapa/teatro.png'

def kml_teatro_municipio(request, codigo_ibge):
    '''Lista em KML todas os teatros do municipio'''

    from teatro.models import Teatro
    from ibge.models import Municipio
    import simplekml

    mun = Municipio.objects.get(cd_geocodm = int(codigo_ibge))

    poi = Teatro.objects.filter(geom__intersects = mun.area)

    kml = simplekml.Kml()

    for e in poi:
        pnt = kml.newpoint(
            name = unicode(e.nome),
            description = '/teatro/' + unicode(e.id),
            coords = [(e.geom.x, e.geom.y)]
            )
        pnt.style.iconstyle.scale = 1
        pnt.style.iconstyle.icon.href = icone

    return HttpResponse(kml.kml(), mimetype='Content-Type:application/vnd.google-earth.kml+xml')


def kml_territorio(request, codigo_inep):
    '''POI Teatro'''

    from django.contrib.gis.measure import Distance, D
    from escola.models import Escola
    from teatro.models import Teatro
    from django.contrib.gis.geos import Point, Polygon, MultiPolygon
    import simplekml

    kml = simplekml.Kml()

    escola = Escola.objects.get(codigo_inep=int(codigo_inep))

    d = Distance(km=1)

    pontos = Teatro.objects.filter(geom__distance_lte=(escola.latlong, d))

    for p in pontos:
        pnt = kml.newpoint(
            name=unicode(p.nome),
            description='/teatro/' + str(p.id),
            coords=[(p.geom.x, p.geom.y)])
        pnt.style.iconstyle.scale = 1
        pnt.style.iconstyle.icon.href = icone

    return HttpResponse(kml.kml(), mimetype='Content-Type:application/vnd.google-earth.kml+xml')


def detalhes(request, codigo):
    '''Tela de detalhe dos Teatros'''

    from teatro.models import Teatro
    from sniic.models import Tipologia
    from territorio.models import TipoGeo

    teatro = Teatro.objects.get(id = int(codigo))

    longitude = str(teatro.geom.x).replace(',','.')
    latitude = str(teatro.geom.y).replace(',','.')

    s1 = teatro.sniic_n1
    if not '.' in s1:
        s1 = s1 + '.'
    s2 = teatro.sniic_n2
    s3 = teatro.sniic_n3

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

    return render_to_response('teatro/detalhes.html', {
        'teatro': teatro,
        'icone': icone,
        'latitude': latitude,
        'longitude': longitude,
        'nome_ponto': 'Teatro',
        'sniic1': sniic1,
        'sniic2': sniic2,
        'sniic3': sniic3,
        })