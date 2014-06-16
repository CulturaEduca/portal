# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.gis import admin
from django.contrib.gis.db import models
from ibge.models import Municipio
from territorio.models import TipoGeo
from referencia.models import TipoEsfera
from sniic.models import Nivel3


class DiaFuncionamento(models.Model):
    '''Dias de funcionamento'''

    dia = models.CharField('Dia de funcionamento', max_length=10)

    def __unicode__(self):
        return self.dia

class PeriodoFuncionamento(models.Model):
    '''Periodos de funcionamento'''

    periodo = models.CharField('Periodo de Funcionamento', max_length=20)

    def __unicode__(self):
        return self.periodo


class Biblioteca(models.Model):
    '''
    Novo models de Bibliotecas, com base nos CSV,
    esse passa a vigorar assim que migrar todas as refs
    para esse.
    
    TODO: migrar views
    '''

    id = models.IntegerField(primary_key=True)
    codigo_equipamento = models.IntegerField('Codigo do Equipamento', max_length=9, null=True, blank=True)
    nome = models.CharField('Nome da Biblioteca', max_length=200, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=20, null=True, blank=True)    
    longitude = models.FloatField('Longitude', null = True, blank = True)
    latitude = models.FloatField('Latitude', null = True, blank = True)
    tipogeo = models.ForeignKey(TipoGeo)
    ibge = models.ForeignKey(Municipio, null=True, blank=True, db_column='ibge')

    endereco_original = models.CharField('Endereco Original', max_length=200, null=True, blank=True)
    numero_original = models.CharField('Numero Original', max_length=200, null=True, blank=True)
    complemento_original = models.CharField('Complemento Original', max_length=200, null=True, blank=True)
    bairro_original = models.CharField('Bairro Original', max_length=200, null=True, blank=True)
    cep_original = models.CharField('CEP Orignal', max_length=30, null=True, blank=True)
  
    tipo_logradouro = models.CharField('Tipo de Logradouro', max_length=20, null=True, blank=True)
    nome_logradouro = models.CharField('Endereco', max_length=100, null=True, blank=True)
    numero_logradouro = models.CharField('Numero', max_length=20, null=True, blank=True)
    km = models.CharField('KM', max_length=20, null=True, blank=True)
    complemento_original = models.CharField('Complemento', max_length=200, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=100, null=True, blank=True)
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)

    ddd_telefone1 = models.CharField('DDD Telefone', max_length=3, null=True, blank=True)
    telefone1 = models.CharField('Telefone1', max_length=10, null=True, blank=True)
    ddd_telefone2 = models.CharField('DDD Telefone 2', max_length=3, null=True, blank=True)
    telefone2 = models.CharField('Telefone1', max_length=10, null=True, blank=True)
    ddd_telefone3 = models.CharField('DDD Telefone 3', max_length=3, null=True, blank=True)
    telefone3 = models.CharField('Telefone1', max_length=10, null=True, blank=True)

    ddd_fax = models.CharField('DDD Fax', max_length=3, null=True, blank=True)
    fax = models.CharField('FAX', max_length=10, null=True, blank=True)

    email1 = models.EmailField('Email 1', null=True, blank=True)
    email2 = models.EmailField('Email 2', null=True, blank=True)
    email3 = models.EmailField('Email 3', null=True, blank=True)

    tipo_esfera = models.ForeignKey(TipoEsfera, null=True, blank=True)
    mantenedor = models.CharField('Mantenedor', max_length=200, null=True, blank=True)
    cnpj_mantenedor = models.CharField('CNPJ Mantenedor', max_length=20, null=True, blank=True)

    sniic_n1 = models.CharField('SNIIC N1', max_length=10, null=True, blank=True)
    sniic_n2 = models.CharField('SNIIC N2', max_length=10, null=True, blank=True)
    sniic_n3 = models.CharField('SNIIC N3', max_length=10, null=True, blank=True)

    tipologia_sniic = models.ForeignKey(Nivel3, null=True, blank=True)

    site = models.CharField('Site', max_length=200, null=True, blank=True)

    # Especifico dessa base
    codigo_biblioteca = models.CharField('Codigo Biblioteca', max_length=20, null=True, blank=True)
    nome_responsavel = models.CharField('Nome Responsavel', max_length=100, null=True, blank=True)
    cod_censo_fgv = models.CharField('Codigo Censo FGV', max_length=10, null=True, blank=True)
    dias_funcionamento = models.ManyToManyField('DiaFuncionamento', null=True, blank=True)
    periodo_funcionamento = models.ManyToManyField('PeriodoFuncionamento', null=True, blank=True)
    acesso_usuario_internet = models.BooleanField('Acesso a Internet')
    qtd_emprestimos_domiciliar = models.IntegerField('Quantidade de Emprestimos', null=True, blank=True)
    acervo_livros = models.IntegerField('Quantidade de livros', null=True, blank=True)
    geom = models.GeometryField(null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nome


#admin.site.register(Biblioteca)
admin.site.register(DiaFuncionamento)
admin.site.register(PeriodoFuncionamento)
admin.site.register(Biblioteca)

# Teste Atom
