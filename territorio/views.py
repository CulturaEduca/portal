# -*- coding: utf-8 -*-

from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from geopy.distance import distance as geopy_distance

def lista(request):
    '''Lista todas escolas ativas'''


    return render_to_response('territorio/lista.html', {})

def detalhe(request, codigo_inep):
	'''Essa rotina monta o territorio educativo com base no codigo inep da escola'''

	from django.contrib.gis.geos import GEOSGeometry
	from django.contrib.gis.geos import Point, Polygon, MultiPolygon
	from django.contrib.gis.measure import Distance, D
	from escola.models import Escola 
	from ibge.models import Municipio
	from ibge.models import SetorCensitario
	from censo_ibge.models import Domicilio01PorSetor
	from censo_ibge.models import Domicilio02PorSetor
	from censo_ibge.models import Responsavel01PorSetor
	from censo_ibge.models import Responsavel02PorSetor
	from censo_ibge.models import ResponsavelrendaPorSetor
	from censo_ibge.models import DomiciliorendaPorSetor
	from censo_ibge.models import PessoarendaPorSetor
	from censo_ibge.models import BasicoPorSetor
	from censo_ibge.models import Pessoa11PorSetor
	from censo_ibge.models import Pessoa12PorSetor
	from censo_ibge.models import Entorno01PorSetor
	from censo_ibge.models import Entorno02PorSetor
	from censo_ibge.models import Entorno03PorSetor
	from censo_ibge.models import Pessoa01PorSetor
	from censo_ibge.models import Pessoa02PorSetor
	from censo_ibge.models import Pessoa03PorSetor
	from escola.models import DadosEscolas
	from ideb.models import Ideb

	escola = Escola.objects.get(codigo_inep = codigo_inep)
	dados_escolas = DadosEscolas.objects.get(cod_inep = codigo_inep)

	ll_e = (escola.longitude, escola.latitude)

	latitude = str(escola.latitude).replace(',','.')
	longitude = str(escola.longitude).replace(',','.')

	# Pega o raio personalizado do municipio
	raio = Municipio.objects.get(cd_geocodm = escola.ibge.cd_geocodm).raio
	if raio == None:
		raio = 1

	# Calculos censo IBGE
	distancia_raio = Distance(km = raio)
	try:
		todos_setores = SetorCensitario.objects.filter(
			cd_geocodm = escola.ibge.cd_geocodm).filter(
			setor_censitario_bruto__distance_lte=(escola.latlong, distancia_raio))
	except:
		todos_setores = []
	
	domicilio_por_setor = {
	'casas': 0,
	'apartamentos': 0,
	'sem_agua': 0,
	'sem_banheiro': 0,
	'sem_lixo': 0,
	'sem_energia': 0,
	'casas_p': 0,
	'apartamentos_p': 0,
	'sem_agua_p': 0,
	'sem_banheiro_p': 0,
	'sem_lixo_p': 0,
	'sem_energia_p': 0,
	}

	moradores = {
	'casas': 0,
	'apartamentos': 0,
	'sem_agua': 0,
	'sem_banheiro': 0,
	'sem_lixo': 0,
	'sem_energia': 0,
	'casas_p': 0,
	'apartamentos_p': 0,
	'sem_agua_p': 0,
	'sem_banheiro_p': 0,
	'sem_lixo_p': 0,
	'sem_energia_p': 0,	
	}

	responsaveis = {
	'h_responsaveis': 0,
	'h_nao_alfabetizados': 0,
	'h_ate_18': 0,
	'h_sem_rendimento': 0,
	'h_rendimento_1sm': 0,
	'h_responsaveis_p': 0,
	'h_nao_alfabetizados_p': 0,
	'h_ate_18_p': 0,
	'h_sem_rendimento_p': 0,
	'h_rendimento_1sm_p': 0,
	'm_responsaveis': 0,
	'm_nao_alfabetizados': 0,
	'm_ate_18': 0,
	'm_sem_rendimento': 0,
	'm_rendimento_1sm': 0,
	'm_responsaveis_p': 0,
	'm_nao_alfabetizados_p': 0,
	'm_ate_18_p': 0,
	'm_sem_rendimento_p': 0,
	'm_rendimento_1sm_p': 0,
	't_responsaveis': 0,
	't_nao_alfabetizados': 0,
	't_ate_18': 0,
	't_sem_rendimento': 0,
	't_rendimento_1sm': 0,
	't_responsaveis_p': 0,
	't_nao_alfabetizados_p': 0,
	't_ate_18_p': 0,
	't_sem_rendimento_p': 0,
	't_rendimento_1sm_p': 0,
	}

	renda = {
	'dom_sem_rendimento': 0,
	'dom_ate_meio': 0,
	'dom_de_meio_a_1': 0,
	'dom_de_1_a_2': 0,
	'dom_de_2_a_3': 0,
	'dom_de_3_a_5': 0,
	'dom_de_5_a_10': 0,
	'dom_de_10_a_15': 0,
	'dom_de_15_a_20': 0,
	'dom_mais_de_20': 0,
	'dom_sem_rendimento_p': 0,
	'dom_ate_meio_p': 0,
	'dom_de_meio_a_1_p': 0,
	'dom_de_1_a_2_p': 0,
	'dom_de_2_a_3_p': 0,
	'dom_de_3_a_5_p': 0,
	'dom_de_5_a_10_p': 0,
	'dom_de_10_a_15_p': 0,
	'dom_de_15_a_20_p': 0,
	'dom_mais_de_20_p': 0,
	'h_sem_rendimento': 0,
	'h_ate_meio': 0,
	'h_de_meio_a_1': 0,
	'h_de_1_a_2': 0,
	'h_de_2_a_3': 0,
	'h_de_3_a_5': 0,
	'h_de_5_a_10': 0,
	'h_de_10_a_15': 0,
	'h_de_15_a_20': 0,
	'h_mais_de_20': 0,
	'm_sem_rendimento': 0,
	'm_ate_meio': 0,
	'm_de_meio_a_1': 0,
	'm_de_1_a_2': 0,
	'm_de_2_a_3': 0,
	'm_de_3_a_5': 0,
	'm_de_5_a_10': 0,
	'm_de_10_a_15': 0,
	'm_de_15_a_20': 0,
	'm_mais_de_20': 0,
	}

	piramide = {
	'h_100_mais': 0,
	'h_95_99': 0,
	'h_90_94': 0,
	'h_85_89': 0,
	'h_80_84': 0,
	'h_75_79': 0,
	'h_70_74': 0,
	'h_65_69': 0,
	'h_60_64': 0,
	'h_55_59': 0,
	'h_50_54': 0,
	'h_45_49': 0,
	'h_40_44': 0,
	'h_35_39': 0,
	'h_30_34': 0,
	'h_25_29': 0,
	'h_20_24': 0,
	'h_15_19': 0,
	'h_10_14': 0,
	'h_5_9': 0,
	'h_0_4': 0,
	'm_100_mais': 0,
	'm_95_99': 0,
	'm_90_94': 0,
	'm_85_89': 0,
	'm_80_84': 0,
	'm_75_79': 0,
	'm_70_74': 0,
	'm_65_69': 0,
	'm_60_64': 0,
	'm_55_59': 0,
	'm_50_54': 0,
	'm_45_49': 0,
	'm_40_44': 0,
	'm_35_39': 0,
	'm_30_34': 0,
	'm_25_29': 0,
	'm_20_24': 0,
	'm_15_19': 0,
	'm_10_14': 0,
	'm_5_9': 0,
	'm_0_4': 0,
	}

	infra = {
	'd_arborizacao_s': 0,
	'd_calcada_s': 0,
	'd_iluminacao_s': 0,
	'd_pavimentacao_s': 0,
	'd_rampa_cadeirante_s': 0,
	'd_esgoto_s': 0,
	'd_lixo_s': 0,
	'm_arborizacao_s': 0,
	'm_calcada_s': 0,
	'm_iluminacao_s': 0,
	'm_pavimentacao_s': 0,
	'm_rampa_cadeirante_s': 0,
	'm_esgoto_s': 0,
	'm_lixo_s': 0,
	'd_arborizacao_n': 0,
	'd_calcada_n': 0,
	'd_iluminacao_n': 0,
	'd_pavimentacao_n': 0,
	'd_rampa_cadeirante_n': 0,
	'd_esgoto_n': 0,
	'd_lixo_n': 0,
	'm_arborizacao_n': 0,
	'm_calcada_n': 0,
	'm_iluminacao_n': 0,
	'm_pavimentacao_n': 0,
	'm_rampa_cadeirante_n': 0,
	'm_esgoto_n': 0,
	'm_lixo_n': 0,

	}

	alfab = {
	'h_5_9_s': 0,
	'h_10_14_s': 0,
	'h_15_19_s': 0,
	'h_20_24_s': 0,
	'h_25_29_s': 0,
	'h_30_34_s': 0,
	'h_35_39_s': 0,
	'h_40_44_s': 0,
	'h_45_49_s': 0,
	'h_50_54_s': 0,
	'h_55_59_s': 0,
	'h_60_64_s': 0,
	'h_65_69_s': 0,
	'h_70_74_s': 0,
	'h_75_79_s': 0,
	'h_mais80_s': 0,
	'm_5_9_s': 0,
	'm_10_14_s': 0,
	'm_15_19_s': 0,
	'm_20_24_s': 0,
	'm_25_29_s': 0,
	'm_30_34_s': 0,
	'm_35_39_s': 0,
	'm_40_44_s': 0,
	'm_45_49_s': 0,
	'm_50_54_s': 0,
	'm_55_59_s': 0,
	'm_60_64_s': 0,
	'm_65_69_s': 0,
	'm_70_74_s': 0,
	'm_75_79_s': 0,
	'm_mais80_s': 0,
	'h_5_9_n': 0,
	'h_10_14_n': 0,
	'h_15_19_n': 0,
	'h_20_24_n': 0,
	'h_25_29_n': 0,
	'h_30_34_n': 0,
	'h_35_39_n': 0,
	'h_40_44_n': 0,
	'h_45_49_n': 0,
	'h_50_54_n': 0,
	'h_55_59_n': 0,
	'h_60_64_n': 0,
	'h_65_69_n': 0,
	'h_70_74_n': 0,
	'h_75_79_n': 0,
	'h_mais80_n': 0,
	'm_5_9_n': 0,
	'm_10_14_n': 0,
	'm_15_19_n': 0,
	'm_20_24_n': 0,
	'm_25_29_n': 0,
	'm_30_34_n': 0,
	'm_35_39_n': 0,
	'm_40_44_n': 0,
	'm_45_49_n': 0,
	'm_50_54_n': 0,
	'm_55_59_n': 0,
	'm_60_64_n': 0,
	'm_65_69_n': 0,
	'm_70_74_n': 0,
	'm_75_79_n': 0,
	'm_mais80_n': 0,
	}

	raca = {
	'branca': 0,
	'preta': 0,
	'amarela': 0,
	'parda': 0,
	'indigena': 0,
	}


	for s in todos_setores:
		try:
			racacor = Pessoa03PorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))
			raca['branca'] += racacor.v002
			raca['preta'] += racacor.v003
			raca['amarela'] += racacor.v004
			raca['parda'] += racacor.v005
			raca['indigena'] += racacor.v006
		except:
			pass

		try:
			dom01 = Domicilio01PorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))
			domicilio_por_setor['casas'] += dom01.s001
			domicilio_por_setor['apartamentos'] += dom01.v005
			domicilio_por_setor['sem_agua'] += dom01.s004
			domicilio_por_setor['sem_banheiro'] += dom01.v023
			domicilio_por_setor['sem_lixo'] += dom01.s005
			domicilio_por_setor['sem_energia'] += dom01.v046
			domicilio_por_setor['casas_p'] += dom01.ps001 / len(todos_setores)
			domicilio_por_setor['apartamentos_p'] += dom01.pv005 / len(todos_setores)
			domicilio_por_setor['sem_agua_p'] += dom01.ps004 / len(todos_setores)
			domicilio_por_setor['sem_banheiro_p'] += dom01.pv023 / len(todos_setores)
			domicilio_por_setor['sem_lixo_p'] += dom01.ps005 / len(todos_setores)
			domicilio_por_setor['sem_energia_p'] += dom01.pv046 / len(todos_setores)
		except:
			pass

		try:
			mor01 = Domicilio02PorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))
			moradores['casas'] += mor01.s001
			moradores['apartamentos'] += mor01.v005
			moradores['sem_agua'] += mor01.s004
			moradores['sem_banheiro'] += mor01.v023
			moradores['sem_lixo'] += mor01.s005
			moradores['sem_energia'] += mor01.v041
			moradores['casas_p'] += mor01.ps001 / len(todos_setores)
			moradores['apartamentos_p'] += mor01.pv005 / len(todos_setores)
			moradores['sem_agua_p'] += mor01.ps004 / len(todos_setores)
			moradores['sem_banheiro_p'] += mor01.pv023 / len(todos_setores)
			moradores['sem_lixo_p'] += mor01.ps005 / len(todos_setores)
			moradores['sem_energia_p'] += mor01.pv041 / len(todos_setores)
		except:
			pass


		try:
			r01 = Responsavel01PorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))
			r02 = Responsavel02PorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))
			rrenda = ResponsavelrendaPorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))

	
			responsaveis['h_responsaveis'] += r02.v109
			responsaveis['h_responsaveis_p'] += r02.pv109 / len(todos_setores)
			responsaveis['h_nao_alfabetizados'] += r02.s004
			responsaveis['h_nao_alfabetizados_p'] += r02.ps004 / len(todos_setores)
			responsaveis['h_ate_18'] += r02.s003
			responsaveis['h_ate_18_p'] += r02.ps003 / len(todos_setores)
			responsaveis['h_sem_rendimento'] += rrenda.v032
			responsaveis['h_sem_rendimento_p'] += rrenda.pv032 / len(todos_setores)
			responsaveis['h_rendimento_1sm'] += rrenda.s002
			responsaveis['h_rendimento_1sm_p'] += rrenda.ps002 / len(todos_setores)
			responsaveis['m_responsaveis'] += r01.v001
			responsaveis['m_responsaveis_p'] += r01.pv001 / len(todos_setores)
			responsaveis['m_nao_alfabetizados'] += r01.s002
			responsaveis['m_nao_alfabetizados_p'] += r01.ps002 / len(todos_setores)
			responsaveis['m_ate_18'] += r01.s001
			responsaveis['m_ate_18_p'] += r01.ps001 / len(todos_setores)
			responsaveis['m_sem_rendimento'] += rrenda.v054
			responsaveis['m_sem_rendimento_p'] += rrenda.pv054 / len(todos_setores)
			responsaveis['m_rendimento_1sm'] += rrenda.s003
			responsaveis['m_rendimento_1sm_p'] += rrenda.ps003 / len(todos_setores)
			responsaveis['t_responsaveis'] += r02.v001
			#responsaveis['t_responsaveis_p'] += r02.pv001 / len(todos_setores)
			responsaveis['t_nao_alfabetizados'] += r02.s002
			#responsaveis['t_nao_alfabetizados_p'] += r02.ps002 / len(todos_setores)
			responsaveis['t_ate_18'] += r02.s001
			#responsaveis['t_ate_18_p'] += r02.ps001 / len(todos_setores)
			responsaveis['t_sem_rendimento'] += rrenda.v010
			responsaveis['t_sem_rendimento_p'] += rrenda.pv010 / len(todos_setores)
			responsaveis['t_rendimento_1sm'] += rrenda.s001
			responsaveis['t_rendimento_1sm_p'] += rrenda.ps001 / len(todos_setores)
		except:
			pass

		try:
			drenda = DomiciliorendaPorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))
		except:
			drenda = False
			pass
		try:
			prenda = PessoarendaPorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))
		except:
			prenda = False
			pass
		try:
			basico_setor = BasicoPorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))
		except:
			basico_setor = False
			pass

		if drenda:
			renda['dom_sem_rendimento'] += drenda.v014
			renda['dom_ate_meio'] += drenda.s001
			renda['dom_de_meio_a_1'] += drenda.v008
			renda['dom_de_1_a_2'] += drenda.v009
			renda['dom_de_2_a_3'] += drenda.v010
			renda['dom_de_3_a_5'] += drenda.v011
			renda['dom_de_5_a_10'] += drenda.v012
			renda['dom_de_10_a_15'] += drenda.v013

		if prenda:
			renda['h_sem_rendimento'] += prenda.v032
			renda['h_ate_meio'] += prenda.v023
			renda['h_de_meio_a_1'] += prenda.v024
			renda['h_de_1_a_2'] += prenda.v025
			renda['h_de_2_a_3'] += prenda.v026
			renda['h_de_3_a_5'] += prenda.v027
			renda['h_de_5_a_10'] += prenda.v028
			renda['h_de_10_a_15'] += prenda.v029
			renda['h_de_15_a_20'] += prenda.v030
			renda['h_mais_de_20'] += prenda.v031

			renda['m_sem_rendimento'] += prenda.v054
			renda['m_ate_meio'] += prenda.v045
			renda['m_de_meio_a_1'] += prenda.v046
			renda['m_de_1_a_2'] += prenda.v047
			renda['m_de_2_a_3'] += prenda.v048
			renda['m_de_3_a_5'] += prenda.v049
			renda['m_de_5_a_10'] += prenda.v050
			renda['m_de_10_a_15'] += prenda.v051
			renda['m_de_15_a_20'] += prenda.v052
			renda['m_mais_de_20'] += prenda.v053

		try:
			psetor = Pessoa11PorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))
			psetor2 = Pessoa12PorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))

			piramide['h_100_mais'] += psetor.v134
			piramide['h_95_99'] += psetor.s020
			piramide['h_90_94'] += psetor.s019
			piramide['h_85_89'] += psetor.s018
			piramide['h_80_84'] += psetor.s017
			piramide['h_75_79'] += psetor.s016
			piramide['h_70_74'] += psetor.s015
			piramide['h_65_69'] += psetor.s014
			piramide['h_60_64'] += psetor.s013
			piramide['h_55_59'] += psetor.s012
			piramide['h_50_54'] += psetor.s011
			piramide['h_45_49'] += psetor.s010
			piramide['h_40_44'] += psetor.s009
			piramide['h_35_39'] += psetor.s008
			piramide['h_30_34'] += psetor.s007
			piramide['h_25_29'] += psetor.s006
			piramide['h_20_24'] += psetor.s005
			piramide['h_15_19'] += psetor.s004
			piramide['h_10_14'] += psetor.s003
			piramide['h_5_9'] += psetor.s002
			piramide['h_0_4'] += psetor.s001

			piramide['m_100_mais'] += psetor.v134
			piramide['m_95_99'] += psetor2.s020
			piramide['m_90_94'] += psetor2.s019
			piramide['m_85_89'] += psetor2.s018
			piramide['m_80_84'] += psetor2.s017
			piramide['m_75_79'] += psetor2.s016
			piramide['m_70_74'] += psetor2.s015
			piramide['m_65_69'] += psetor2.s014
			piramide['m_60_64'] += psetor2.s013
			piramide['m_55_59'] += psetor2.s012
			piramide['m_50_54'] += psetor2.s011
			piramide['m_45_49'] += psetor2.s010
			piramide['m_40_44'] += psetor2.s009
			piramide['m_35_39'] += psetor2.s008
			piramide['m_30_34'] += psetor2.s007
			piramide['m_25_29'] += psetor2.s006
			piramide['m_20_24'] += psetor2.s005
			piramide['m_15_19'] += psetor2.s004
			piramide['m_10_14'] += psetor2.s003
			piramide['m_5_9'] += psetor2.s002
			piramide['m_0_4'] += psetor2.s001
		except:
			pass

		try:
			entorno01 = Entorno01PorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))
			entorno02 = Entorno03PorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))
			infra['d_arborizacao_s'] += entorno01.s015
			infra['d_calcada_s'] += entorno01.s007
			infra['d_pavimentacao_s'] += entorno01.s005
			infra['d_rampa_cadeirante_s'] += entorno01.s013
			infra['d_esgoto_s'] += entorno01.s017
			infra['d_lixo_s'] += entorno01.s019 
			infra['d_iluminacao_s'] += entorno01.s003

			infra['d_arborizacao_n'] += entorno01.s016
			infra['d_calcada_n'] += entorno01.s008
			infra['d_pavimentacao_n'] += entorno01.s006
			infra['d_rampa_cadeirante_n'] += entorno01.s014
			infra['d_esgoto_n'] += entorno01.s018
			infra['d_lixo_n'] += entorno01.s020 
			infra['d_iluminacao_n'] += entorno01.s004

			infra['m_arborizacao_s'] += entorno02.s015
			infra['m_calcada_s'] += entorno02.s007
			infra['m_pavimentacao_s'] += entorno02.s005
			infra['m_rampa_cadeirante_s'] += entorno02.s013
			infra['m_esgoto_s'] += entorno02.s017
			infra['m_lixo_s'] += entorno02.s019 
			infra['m_iluminacao_s'] += entorno02.s003

			infra['m_arborizacao_n'] += entorno02.s016
			infra['m_calcada_n'] += entorno02.s008
			infra['m_pavimentacao_n'] += entorno02.s006
			infra['m_rampa_cadeirante_n'] += entorno02.s014
			infra['m_esgoto_n'] += entorno02.s018
			infra['m_lixo_n'] += entorno02.s020 
			infra['m_iluminacao_n'] += entorno02.s004


		except:
			pass

		try:
			p01 = Pessoa02PorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))
			p02 = Pessoa01PorSetor.objects.using('censo_ibge').get(cod_setor = float(s.cd_geocodi))

			alfab['h_5_9_s'] += p01.s001
			alfab['h_10_14_s'] += p01.s002
			alfab['h_15_19_s'] += p01.s003
			alfab['h_20_24_s'] += p01.s004
			alfab['h_25_29_s'] += p01.s005
			alfab['h_30_34_s'] += p01.s006
			alfab['h_35_39_s'] += p01.s007
			alfab['h_40_44_s'] += p01.s008
			alfab['h_45_49_s'] += p01.s009
			alfab['h_50_54_s'] += p01.s010
			alfab['h_55_59_s'] += p01.s011
			alfab['h_60_64_s'] += p01.s012
			alfab['h_65_69_s'] += p01.s013
			alfab['h_70_74_s'] += p01.s014
			alfab['h_75_79_s'] += p01.s015
			alfab['h_mais80_s'] += p01.v077

			alfab['m_5_9_s'] += p01.s032
			alfab['m_10_14_s'] += p01.s033
			alfab['m_15_19_s'] += p01.s034
			alfab['m_20_24_s'] += p01.s035
			alfab['m_25_29_s'] += p01.s036
			alfab['m_30_34_s'] += p01.s037
			alfab['m_35_39_s'] += p01.s038
			alfab['m_40_44_s'] += p01.s039
			alfab['m_45_49_s'] += p01.s040
			alfab['m_50_54_s'] += p01.s041
			alfab['m_55_59_s'] += p01.s042
			alfab['m_60_64_s'] += p01.s043
			alfab['m_65_69_s'] += p01.s044
			alfab['m_70_74_s'] += p01.s045
			alfab['m_75_79_s'] += p01.s046
			alfab['m_mais80_s'] += p01.v162

			alfab['h_5_9_n'] += p01.s016
			alfab['h_10_14_n'] += p01.s017
			alfab['h_15_19_n'] += p01.s018
			alfab['h_20_24_n'] += p01.s019
			alfab['h_25_29_n'] += p01.s020
			alfab['h_30_34_n'] += p01.s021
			alfab['h_35_39_n'] += p01.s022
			alfab['h_40_44_n'] += p01.s023
			alfab['h_45_49_n'] += p01.s024
			alfab['h_50_54_n'] += p01.s025
			alfab['h_55_59_n'] += p01.s026
			alfab['h_60_64_n'] += p01.s027
			alfab['h_65_69_n'] += p01.s028
			alfab['h_70_74_n'] += p01.s029
			alfab['h_75_79_n'] += p01.s030
			alfab['h_mais80_n'] += p01.s031

			alfab['m_5_9_n'] += p01.s047
			alfab['m_10_14_n'] += p01.s048
			alfab['m_15_19_n'] += p01.s049
			alfab['m_20_24_n'] += p01.s050
			alfab['m_25_29_n'] += p01.s051
			alfab['m_30_34_n'] += p01.s052
			alfab['m_35_39_n'] += p01.s053
			alfab['m_40_44_n'] += p01.s054
			alfab['m_45_49_n'] += p01.s055
			alfab['m_50_54_n'] += p01.s056
			alfab['m_55_59_n'] += p01.s057
			alfab['m_60_64_n'] += p01.s058
			alfab['m_65_69_n'] += p01.s059
			alfab['m_70_74_n'] += p01.s060
			alfab['m_75_79_n'] += p01.s061
			alfab['m_mais80_n'] += p01.s062
		except:
			pass

	# Pega os equipamentos de saude
	from saude.models import Saude

	equipamentos_saude = []
	
	try: 
		for p in Saude.objects.filter(geom__distance_lte = (escola.latlong, distancia_raio)):
			ll_p = (p.longitude, p.latitude)
			distancia = geopy_distance(ll_e, ll_p).meters
			equipamentos_saude.append({
				'nome': p.nome,
				'tipo_logradouro': p.tipo_logra,
				'nome_logradouro': p.nome_logra,
				'numero_logradouro': p.num_lograd,
				'id': p.id,
				'distancia': distancia,
				})
	except:
		pass

	# Pega os teatros
	from teatro.models import Teatro

	teatros = []

	try:
		for p in Teatro.objects.filter(geom__distance_lte = (escola.latlong, distancia_raio)):
			ll_p = (p.longitude, p.latitude)
			distancia = geopy_distance(ll_e, ll_p).meters
			teatros.append({
				'nome': p.nome,
				'tipo_logradouro': p.tipo_logradouro,
				'nome_logradouro': p.nome_logradouro,
				'numero_logradouro': p.numero_logradouro,
				'id': p.id,
				'distancia': distancia
				})
	except:
		pass

	# pega os museus
	from museu.models import Museu

	museus = []

	try:
		for p in Museu.objects.filter(geom__distance_lte = (escola.latlong, distancia_raio)):
			ll_p = (p.longitude, p.latitude)
			distancia = geopy_distance(ll_e, ll_p).meters
			museus.append({
				'nome': p.nome,
				'tipo_logradouro': p.tipo_logradouro,
				'nome_logradouro': p.nome_logradouro,
				'numero_logradouro': p.numero_logradouro,
				'id': p.id,
				'distancia': distancia
				})

	except:
		pass

	# Pega as bibliotecas
	from biblioteca.models import Biblioteca

	bibliotecas = []

	try:
		for p in Biblioteca.objects.filter(geom__distance_lte = (escola.latlong, distancia_raio)):
			ll_p = (p.longitude, p.latitude)
			distancia = geopy_distance(ll_e, ll_p).meters
			bibliotecas.append({
				'nome': p.nome,
				'tipo_logradouro': p.tipo_logradouro,
				'nome_logradouro': p.nome_logradouro,
				'numero_logradouro': p.numero_logradouro,
				'id': p.id,
				'distancia': distancia
				})

	except:
		pass

	# Pega os centros de ciencia
	from centro_ciencia.models import CentroCiencia

	centros_ciencia = []

	try: 
		for p in CentroCiencia.objects.filter(geom__distance_lte = (escola.latlong, distancia_raio)):
			ll_p = (p.longitude, p.latitude)
			distancia = geopy_distance(ll_e, ll_p).meters
			centros_ciencia.append({
				'nome': p.nome,
				'tipo_logradouro': p.tipo_logradouro,
				'nome_logradouro': p.nome_logradouro,
				'numero_logradouro': p.numero_logradouro,
				'id': p.id,
				'distancia': distancia
				})

	except:
		pass

	# Pega CRAs
	from cra.models import Cra
	try:
		cras = Cra.objects.filter(geom__distance_lte = (escola.latlong, distancia_raio))
	except:
		cras = []

	# Pega os cinemas
	from cinema.models import Cinema

	cinemas = []

	try:
		for p in Cinema.objects.filter(geom__distance_lte = (escola.latlong, distancia_raio)):
			ll_p = (p.longitude, p.latitude)
			distancia = geopy_distance(ll_e, ll_p).meters

			cinemas.append({
				'nome': p.nome,
				'tipo_logradouro': p.tipo_logradouro,
				'nome_logradouro': p.nome_logradouro,
				'numero_logradouro': p.numero_logradouro,
				'id': p.id,
				'distancia': distancia
				})
	except:
		pass

	# Pega as salas verdes
	from sala_verde.models import SalaVerde

	salas_verdes = []

	try:
		for p in SalaVerde.objects.filter(geom__distance_lte = (escola.latlong, distancia_raio)):
			ll_p = (p.longitude, p.latitude)
			distancia = geopy_distance(ll_e, ll_p).meters
			salas_verdes.append({
				'nome': p.nome,
				'endereco': p.nome_logradouro,
				'id': p.id,
				'distancia': distancia				
				})
	except:
		pass

	# Pega os pontos de cultura
	from ponto_cultura.models import PontoCultura

	pontos_cultura = []

	try:
		for p in PontoCultura.objects.filter(geom__distance_lte = (escola.latlong, distancia_raio)).distance(escola.latlong).order_by('distance'):
			ll_p = (p.longitude, p.latitude)
			distancia = geopy_distance(ll_e, ll_p).meters

			pontos_cultura.append({
				'projeto': p.projeto,
				'tipo_logradouro': p.tipo_logradouro,
				'nome_logradouro': p.nome_logradouro,
				'numero_logradouro': p.numero_logradouro,
				'id': p.id,
				'distancia': distancia
				})
	except:
		pass


	# Soma domicilios
	try:
		total_domicilios = domicilio_por_setor['casas'] + domicilio_por_setor['apartamentos']
	except:
		total_domicilios = 0

	try:
		total_moradores = moradores['casas'] + moradores['apartamentos']
	except:
		total_moradores = 0

	try:
		numero_setores = len(todos_setores)
	except:
		numero_setores = 0

	try:
		media_moradores = total_moradores / total_domicilios
	except:
		media_moradores = 0

	ideb = Ideb.objects.get(codigo_inep = codigo_inep)

	return render_to_response('territorio/territorio.html', {
		'escola': escola,
		'latitude': latitude,
		'longitude': longitude,
		'setores': todos_setores,
		'domicilio_por_setor': domicilio_por_setor,
		'moradores': moradores,
		'responsaveis': responsaveis,
		'renda': renda,
		'piramide': piramide,
		'infra': infra,
		'alfab': alfab,
		'dados': dados_escolas,
		'equipamentos_saude': equipamentos_saude,
		'teatros': teatros,
		'museus': museus,
		'cinemas': cinemas,
		'salas_verdes': salas_verdes,
		'pontos_cultura': pontos_cultura,
		'bibliotecas': bibliotecas,
		'centros_ciencia': centros_ciencia,
		'cras': cras,
        'raca': raca,
		'total_domicilios': total_domicilios,
		'total_moradores': total_moradores,
		'numero_setores': numero_setores,
		'media_moradores': media_moradores,
		'ideb': ideb,
		})

def ol(request, codigo_ibge):
	'''Teste usando o OpenLayers'''

	from ibge.models import Municipio

	mun = Municipio.objects.get(cd_geocodm = int(codigo_ibge))
	
	centro_mun = mun.area.centroid

	coords = mun.area.coords
	longitude_centro = str(centro_mun.x).replace(',','.')
	latitude_centro = str(centro_mun.y).replace(',','.')


	return render_to_response('territorio/ol.html', {
		'codigo_ibge': codigo_ibge,
		'longitude_centro': longitude_centro,
		'latitude_centro': latitude_centro,
		})

def geojson(request, codigo_inep):
	'''Gera o territorio educativo com base no codigo INEP'''

	from django.contrib.gis.geos import GEOSGeometry
	from django.contrib.gis.geos import Point, Polygon, MultiPolygon
	from django.contrib.gis.measure import Distance, D

	from ibge.models import Municipio
	from ibge.models import SetorCensitario
	from escola.models import Escola

	escola = Escola.objects.get(codigo_inep = codigo_inep)

	# Pega o raio personalizado do municipio
	raio = Municipio.objects.get(cd_geocodm = escola.ibge.cd_geocodm).raio
	if raio == None:
		raio = 1

	distancia_raio = Distance(km = raio)

	agrupamento_setores = SetorCensitario.objects.filter(
		cd_geocodm = escola.ibge.cd_geocodm).filter(
		setor_censitario_bruto__distance_lte=(escola.latlong, distancia_raio))

	aggs = GEOSGeometry(agrupamento_setores[0].setor_censitario_bruto)
	count = 1
	total = len(agrupamento_setores)
	while count < total:
		aggs = aggs + GEOSGeometry(agrupamento_setores[count].setor_censitario_bruto)
		count += 1

	return HttpResponse(aggs.geojson, mimetype='application/json')

