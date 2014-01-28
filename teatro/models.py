# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.gis import admin
from django.contrib.gis.db import models
from ibge.models import Municipio
from territorio.models import TipoGeo


class EsferaAdministrativa(models.Model):
    '''Esfera Administrativa'''

    nome = models.CharField('Nome Esfera', max_length=100)

    def __unicode__(self):
        return self.nome

class TipoEsfera(models.Model):
    '''Tipo Esfera Administrativa'''

    nome = models.CharField('Tipo Esfera', max_length=200)

    def __unicode__(self):
        return self.nome


class Teatro(models.Model):
    '''Nova modelagem para teatros'''

    id = models.IntegerField(primary_key=True)
    codigo_teatro = models.IntegerField(null = True, blank = True)
    longitude = models.FloatField('Longitude', null = True, blank = True)
    latitude = models.FloatField('Latitude', null = True, blank = True)
    tipogeo = models.ForeignKey(TipoGeo)
    #ibge = models.IntegerField('Codigo IBGE', null=True, blank=True)
    ibge = models.ForeignKey(Municipio, db_column='ibge')
    nome = models.CharField('Nome do Teatro', max_length=200, null=True, blank=True)
    codigo_original = models.CharField('Codigo Original', max_length=200, null=True, blank=True)
    endereco_original = models.CharField('Endereco Original', max_length=200, null=True, blank=True)
    bairro_original = models.CharField('Bairro Original', max_length=200, null=True, blank=True)
    cep_original = models.CharField('CEP Original', max_length=20, null=True, blank=True)
    tipo_logradouro = models.CharField('Tipo de Logradouro', max_length=100, null=True, blank=True)
    nome_logradouro = models.CharField('Endereco', max_length=300, null=True, blank=True)
    km = models.CharField('KM', max_length=200, null=True, blank=True)
    numero_logradouro = models.CharField('Numero', max_length=20, null=True, blank=True)
    complemento_logradouro = models.CharField('Complemento', max_length=200, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=300, null=True, blank=True)
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)
    ddd_telefone1 = models.CharField('DDD Telefone', max_length=3, null=True, blank=True)
    telefone1 = models.CharField('Telefone1', max_length=10, null=True, blank=True)
    telefone2 = models.CharField('Telefone2', max_length=10, null=True, blank=True)
    fax = models.CharField('Fax', max_length=10, null=True, blank=True)    
    email = models.EmailField(null=True, blank=True)
    site = models.CharField('Site', max_length=200, null=True, blank=True)
    esfera_administrativa = models.ForeignKey(EsferaAdministrativa, null=True, blank=True)
    tipo_esfera = models.ForeignKey(TipoEsfera, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=200, null=True, blank=True)
    sniic_n1 = models.CharField('SNIIC N1', max_length=10, null=True, blank=True)
    sniic_n2 = models.CharField('SNIIC N2', max_length=10, null=True, blank=True)
    sniic_n3 = models.CharField('SNIIC N3', max_length=10, null=True, blank=True)
    situacao = models.CharField('Situacao', max_length=10, null=True, blank=True)
    cod_adm = models.CharField('COD ADM', max_length=100, null=True, blank=True)
    tipo = models.CharField('Tipo', max_length=100, null=True, blank=True)
    numero_lugares = models.IntegerField('Numero de Lugares', null=True, blank=True)
    data_inaugacao = models.CharField('Data de Inauguracao', max_length=100, null=True, blank=True)
    ano_inauguracao = models.IntegerField('Ano Inauguracao', blank=True, null=True)
    ano_desaparecimento = models.IntegerField('Ano desaparecimento', blank=True, null=True)
    historia_espaco = models.TextField('Historia do Espaco', null=True, blank=True)
    fonte_original = models.TextField('Fonte original', null=True, blank=True)
    data_info = models.CharField('Data Info', null=True, blank=True, max_length=100)
    geom = models.GeometryField(null=True, blank=True)
    objects = models.GeoManager()


    def __unicode__(self):
        return self.nome


class TeatroAdmin(admin.ModelAdmin):

    raw_id_fields = ('ibge',)

admin.site.register(Teatro,TeatroAdmin)
