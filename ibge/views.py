# -*- encoding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ibge.models import Municipio

def contorno_municipio(request, ibge):
	'''Pega o contorno do municipio'''

	mun = Municipio.objects.get(cd_geocodm = int(ibge))

	return HttpResponse(mun.area.geojson, mimetype='application/json')

def centro_municipio(request, ibge):
	'''Pega a lat/long do centro do municipio para centralizar o mapa'''

	mun = Municipio.objects.get(cd_geocodm = int(ibge))

	return HttpResponse(mun.area.centroid.geojson, mimetype='application/json')

