from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template.defaultfilters import slugify

def uf(request, uf=None):
    '''Busca por UF'''

    from ibge.models import Uf
    from ibge.models import Municipio

    if uf == None:
        lista_uf = Uf.objects.all().order_by('sigla').select_related()
        municipios = None
    else:
        lista_uf = None
        municipios = Municipio.objects.filter(estado__sigla = uf).order_by('nome').select_related()


    return render_to_response('mapa/uf.html', {
        'lista_uf': lista_uf,
        'municipios': municipios,
        'uf': uf,
        })


def municipio(request, uf, municipio):
    '''Detalhe do municipio'''

    from ibge.models import Municipio

    municipio = Municipio.objects.get(estado__sigla = uf, slug = municipio)
    centro_mun = municipio.area.centroid
    coords = municipio.area.coords
    longitude_centro = str(centro_mun.x).replace(',','.')
    latitude_centro = str(centro_mun.y).replace(',','.')

    return render_to_response('mapa/municipio.html',{
        'municipio': municipio,
        'centro_mun': centro_mun,
        'coords': coords,
        'longitude_centro': longitude_centro,
        'latitude_centro': latitude_centro,
        'codigo_ibge': municipio.cd_geocodm,
        'uf': uf,
        })
