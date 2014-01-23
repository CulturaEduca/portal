# -*- coding: utf-8 -*-

from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

def geojson_escolas(request, ibge):
	'''Lista as escolas de um codigo IBGE'''

	from ibge.models import Municipio
	from escola.models import Escola
	from django.utils import simplejson

	feature = {"type":"FeatureCollection","features": []}

	mun = Municipio.objects.get(cd_geocodm = int(ibge))

	escolas = Escola.objects.filter(latlong__intersects = mun.area)
	# escolas = Escola.objects.filter(latitude__isnull = False, longitude__isnull = False)

	for escola in escolas:
		e = {}
		e['type'] = "Feature"
		e['id'] = str(escola.codigo_inep)
		e['geometry'] = {"type": "Point", "coordinates": [escola.longitude, escola.latitude]}
		feature['features'].append(e)

	json = simplejson.dumps(feature)

	# json = [escolas[0].latlong.geojson]

	# for x in escolas:
	# 	json.append(x.latlong.geojson)

	return HttpResponse(json, mimetype='application/json')

def kml_escola(request, codigo_inep):
	'''Gera o KML de uma escola'''

	from escola.models import Escola
	from escola.models import Programa
	import simplekml

	e = Escola.objects.get(codigo_inep = int(codigo_inep))

	# verifica se eh do mais cultura
	prog = Programa.objects.get(pk = 1)
	if prog in e.programas.all():
		mais_cultura = True
	else:
		mais_cultura = False

	kml = simplekml.Kml()

	pnt = kml.newpoint(
		name = e.nome,
		description = e.nome_logradouro,
		coords = [(e.longitude, e.latitude)]
		)

	pnt.style.iconstyle.scale = 1
	if mais_cultura:
		pnt.style.iconstyle.icon.href = '/static/mapa/mais_cultura.png'
	else:
		pnt.style.iconstyle.icon.href = '/static/mapa/escola.png'

	return HttpResponse(kml.kml(), mimetype='Content-Type:application/vnd.google-earth.kml+xml')

def kml_escolas_municipio(request, codigo_ibge):
	'''Lista em KML todas as escolas de um municipio'''

	from escola.models import Escola
	from escola.models import Programa
	from ibge.models import Municipio
	import simplekml

	mun = Municipio.objects.get(cd_geocodm = int(codigo_ibge))

	escolas = Escola.objects.filter(latlong__intersects = mun.area)

	# Verifica se eh mais cultra
	prog = Programa.objects.get(pk = 1)

	kml = simplekml.Kml()

	for e in escolas:
		if prog in e.programas.all():
			mais_cultura = True
		else:
			mais_cultura = False
		pnt = kml.newpoint(
			name = e.nome,
			description = '/territorio/' + str(e.codigo_inep),
			coords = [(e.longitude, e.latitude)]
			)
		pnt.style.iconstyle.scale = 1
		if mais_cultura:
			pnt.style.iconstyle.icon.href = '/static/mapa/mais_cultura.png'
		else:
			pnt.style.iconstyle.icon.href = '/static/mapa/escola.png'

	return HttpResponse(kml.kml(), mimetype='Content-Type:application/vnd.google-earth.kml+xml')
