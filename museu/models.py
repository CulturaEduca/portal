# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.gis import admin
from django.contrib.gis.db import models
from ibge.models import Municipio
from territorio.models import TipoGeo
from referencia.models import TipoEsfera
from sniic.models import Nivel3


class Museu(models.Model):
    '''
    Novo models de Museus, com base nos CSV,
    esse passa a vigorar assim que migrar todas as refs
    para esse.
    
    TODO: migrar views
    '''

    id = models.IntegerField(primary_key=True)
    codigo_equipamento = models.CharField('Codigo do Equipamento', max_length=9, null=True, blank=True)
    nome = models.CharField('Nome da Biblioteca', max_length=300, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=200, null=True, blank=True)

    longitude = models.FloatField('Longitude', null = True, blank = True)
    latitude = models.FloatField('Latitude', null = True, blank = True)
    tipogeo = models.ForeignKey(TipoGeo)
    ibge = models.ForeignKey(Municipio, null=True, blank=True, db_column='ibge')

    endereco_original = models.CharField('Endereco Original', max_length=300, null=True, blank=True)
    endereco_correspondencia = models.CharField('Endereco Original', max_length=300, null=True, blank=True)
    numero_original = models.CharField('Numero Original', max_length=300, null=True, blank=True)
    complemento_original = models.CharField('Complemento Original', max_length=300, null=True, blank=True)
    bairro_original = models.CharField('Bairro Original', max_length=300, null=True, blank=True)
    cep_original = models.CharField('CEP Orignal', max_length=40, null=True, blank=True)
    tipo_logradouro = models.CharField('Tipo de Logradouro', max_length=100, null=True, blank=True)
    nome_logradouro = models.CharField('Endereco', max_length=300, null=True, blank=True)
    km = models.CharField('KM', max_length=200, null=True, blank=True)
    numero_logradouro = models.CharField('Numero', max_length=20, null=True, blank=True)
    complemento_logradouro = models.CharField('Complemento', max_length=200, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=300, null=True, blank=True)
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)

    nome_responsavel = models.CharField('Nome Responsavel', max_length=100, null=True, blank=True)
    ddd_telefone1 = models.CharField('DDD Telefone', max_length=3, null=True, blank=True)
    telefone1 = models.CharField('Telefone1', max_length=10, null=True, blank=True)
    telefone2 = models.CharField('Telefone2', max_length=10, null=True, blank=True)
    telefone3 = models.CharField('Telefone3', max_length=10, null=True, blank=True)
    site = models.CharField('Site', max_length=300, null=True, blank=True)

    tipo_esfera = models.ForeignKey(TipoEsfera, null=True, blank=True)

    sniic_n1 = models.CharField('SNIIC N1', max_length=10, null=True, blank=True)
    sniic_n2 = models.CharField('SNIIC N2', max_length=10, null=True, blank=True)
    sniic_n3 = models.CharField('SNIIC N3', max_length=10, null=True, blank=True)

    tipologia_sniic = models.ForeignKey(Nivel3, null=True, blank=True)

    local = models.CharField('Local', max_length=300, null=True, blank=True)

    # Especifico dessa base
    codigo_museu = models.CharField('Codigo do Museu', max_length=20, null=True, blank=True)

    ano_criacao = models.IntegerField('Ano de Criacao', null=True, blank=True)
    ano_abertura = models.IntegerField('Ano de Abertura', null=True, blank=True)
    orcamento_proprio = models.BooleanField('Orcamento Proprio?')
    qtd_bens_acervo = models.IntegerField('Quantidade de bens no arcevo', null=True, blank=True)
    qtd_bens_exatidao = models.CharField('Precisao da qtd de bens', max_length=300, null=True, blank=True)
    qtd_antropologia_etnografia = models.IntegerField('Acervo Antropologia / Etnografia', null=True, blank=True)
    qtd_arqueologia = models.IntegerField('Acervo Arqueologia', null=True, blank=True)
    qtd_artes_visuais = models.IntegerField('Acervo Artes Visuais', null=True, blank=True)
    qtd_cienciasnaturais_historianatural = models.IntegerField('Acervo Ciencias naturais e Historia Natural', null=True, blank=True)
    qtd_ciencia_tecnologia = models.IntegerField('Acervo Ciencia e Tecnologia', null=True, blank=True)
    qtd_historia = models.IntegerField('Acervo Historia', null=True, blank=True)
    qtd_imagem_som = models.IntegerField('Acervo Imagem e Som', null=True, blank=True)
    qtd_virtual = models.IntegerField('Acervo Virtual', null=True, blank=True)
    qtd_arquivistico = models.IntegerField('Acervo Arquivistico', null=True, blank=True)
    qtd_biblioteconomico = models.IntegerField('Acervo biblioteconomico', null=True, blank=True)
    qtd_documental = models.IntegerField('Acervo Documental', null=True, blank=True)
    qtd_outros = models.IntegerField('Acervo Outros', null=True, blank=True)
    situacao = models.CharField('Situacao', max_length=300, null=True, blank=True)
    ingresso_cobrado = models.BooleanField('Cobra Ingresso?')
    valor_ingresso = models.CharField('Valor do ingresso', max_length=300, null=True, blank=True)
    infra_turista_estrangeiro = models.BooleanField('Infra para turistas estrangeiros?')
    infra_turista_sinalizacao = models.BooleanField('Infra para turistas sinalizacao?')
    sinalizacao_idioma = models.BooleanField('Sinalizacao de Idioma?')
    infra_turistas_etiquetas = models.BooleanField('Infra Turista Etiquetas')
    etiquetas_idioma = models.BooleanField('Etiquetas Idioma')
    infra_turistas_publicacoes = models.BooleanField('Infra turistas publicacoes')
    publicacoes_idioma = models.CharField('Publicacao Idiomas', max_length=300, null=True, blank=True)
    infra_turistas_outros = models.BooleanField('Infra Turista Outros')
    outros_idiomas = models.CharField('Outros Idiomas', max_length=300, null=True, blank=True)
    bebedouro = models.BooleanField('Bebedouro')
    estacionamento = models.BooleanField('Estacionamento')
    lanchonete_restaurante = models.BooleanField('Lanchonete / Restaurante')
    livraria = models.BooleanField('Livraria')
    loja = models.BooleanField('Loja')
    sanitarios = models.BooleanField('Sanitarios')
    telefone_publico = models.BooleanField('Telefone Publico')
    outras_instalacoes1 = models.BooleanField('Outras Instalacoes')
    outras_instalacoes2 = models.CharField('Outras Instalacoes', max_length=300, null=True, blank=True)
    pne_vagas_exclusivas_estacionamento  = models.BooleanField('PNE Vagas Exclusivas Estacionamento')
    pne_elevadores_acessiveis = models.BooleanField('PNE Elevadores Acessiveis')
    pne_rampa_de_acesso = models.BooleanField('PNE Rampa de Acesso')
    pne_sanitarios_adaptados = models.BooleanField('PNE Sanitario Adaptado')
    pne_sinalizacao_braile = models.BooleanField('PNE Sinalizacao Braile')
    pne_etiquetas_braile = models.BooleanField('PNE Etiqueta Braile')
    pne_outros_1 = models.BooleanField('PNE outros 1')
    pne_outros_2 = models.BooleanField('PNE outros 2')
    medidas_preventivas = models.BooleanField('Medidas Preventivas')
    medidas_preventivas_treinamento_profissionais = models.BooleanField('Medidas Preventivas Treinamento Profissional')
    medidas_preventivas_brigada = models.BooleanField('Medida Preventiva Brigada')
    medidas_preventivas_revisao_extintores = models.BooleanField('Medida Preventiva Revisao Extintores')
    medidas_preventivas_revisao_rede_eletrica = models.BooleanField('Medidas Preventivas revisao rede eletrica')
    medidas_preventivas_outras = models.BooleanField('Medida preventiva outras')
    geom = models.GeometryField(null=True, blank=True)
    objects = models.GeoManager()


    def __unicode__(self):
        return self.nome



admin.site.register(Museu)