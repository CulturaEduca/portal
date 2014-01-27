# -*- coding: utf-8 -*-

from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

icone = '/static/mapa/museu.png'

def kml_museu_municipio(request, codigo_ibge):
    '''Lista em KML todas as escolas de um municipio'''

    from museu.models import Museu
    from ibge.models import Municipio
    import simplekml

    mun = Municipio.objects.get(cd_geocodm = int(codigo_ibge))

    poi = Museu.objects.filter(geom__intersects = mun.area)

    kml = simplekml.Kml()

    for e in poi:
        pnt = kml.newpoint(
            name = unicode(e.nome),
            description = '/museu/' + unicode(e.id),
            coords = [(e.geom.x, e.geom.y)]
            )
        pnt.style.iconstyle.scale = 1
        pnt.style.iconstyle.icon.href = icone

    return HttpResponse(kml.kml(), mimetype='Content-Type:application/vnd.google-earth.kml+xml')


def kml_museu_escola(request, codigo_inep):
    '''POI com base na escola'''

    from django.contrib.gis.measure import Distance, D
    from museu.models import Museu
    from escola.models import Escola
    from django.contrib.gis.geos import Point, Polygon, MultiPolygon
    import simplekml

    distancia = Distance(km = 1)

    escola = Escola.objects.get(codigo_inep = codigo_inep)

    ll = escola.latlong

    poi = Museu.objects.filter(geom__distance_lt = (ll, distancia))

    kml = simplekml.Kml()

    for x in poi:
        pnt = kml.newpoint(
            name = unicode(x.nome),
            description = '/museu/' + unicode(x.id),
            coords = [(x.geom.x, x.geom.y)])
        pnt.style.iconstyle.scale = 1
        pnt.style.iconstyle.icon.href = icone


    return HttpResponse(kml.kml(), mimetype='Content-Type:application/vnd.google-earth.kml+xml')

def detalhes(request, codigo):
    '''Tela de detalhe dos Museus'''

    from museu.models import Museu
    from sniic.models import Tipologia

    museu = Museu.objects.get(id = int(codigo))

    s1 = museu.sniic_n1
    if not '.' in s1:
        s1 = s1 + '.'
    s2 = museu.sniic_n2
    s3 = museu.sniic_n3

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



    longitude = str(museu.geom.x).replace(',','.')
    latitude = str(museu.geom.y).replace(',','.')

    return render_to_response('museu/detalhes.html', {
        'museu': museu,
        'icone': icone,
        'latitude': latitude,
        'longitude': longitude,
        'nome_ponto': 'Museu',
        'sniic1': sniic1,
        'sniic2': sniic2,
        'sniic3': sniic3,
        })