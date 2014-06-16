# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.gis import admin
from django.contrib.gis.db import models
from ibge.models import Municipio
from territorio.models import TipoGeo
from referencia.models import TipoEsfera
from sniic.models import Nivel3


class GrupoAncine(models.Model):
    '''Grupo Ancine'''

    nome = models.CharField('Nome Ancine', max_length=200)

    def __unicode__(self):
        return self.nome

class Cinema(models.Model):
    '''Nova modelagem de Cinemas'''

    id = models.IntegerField(primary_key=True)
    codigo_equipamento = models.CharField('Codigo do Equipamento', max_length=9, null=True, blank=True)
    nome = models.CharField('Nome do Equipamento', max_length=300, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=200, null=True, blank=True)    
    longitude = models.FloatField('Longitude', null = True, blank = True)
    latitude = models.FloatField('Latitude', null = True, blank = True)
    tipogeo = models.ForeignKey(TipoGeo)
    ibge = models.ForeignKey(Municipio, null=True, blank=True, db_column='ibge')

    endereco_original = models.CharField('Endereco Original', max_length=300, null=True, blank=True)
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
    ddd_telefone2 = models.CharField('DDD Telefone', max_length=3, null=True, blank=True)
    telefone2 = models.CharField('Telefone2', max_length=10, null=True, blank=True)
    ddd_telefone3 = models.CharField('DDD Telefone', max_length=3, null=True, blank=True)
    telefone3 = models.CharField('Telefone3', max_length=10, null=True, blank=True)
    ddd_fax = models.CharField('DDD FAX', max_length=3, null=True, blank=True)
    fax = models.CharField('FAX', max_length=10, null=True, blank=True)
    site = models.CharField('Site', max_length=300, null=True, blank=True)
    email = models.CharField('Email', max_length=200, null=True, blank=True)

    tipo_esfera = models.ForeignKey(TipoEsfera, null=True, blank=True)

    sniic_n1 = models.CharField('SNIIC N1', max_length=10, null=True, blank=True)
    sniic_n2 = models.CharField('SNIIC N2', max_length=10, null=True, blank=True)
    sniic_n3 = models.CharField('SNIIC N3', max_length=10, null=True, blank=True)

    tipologia_sniic = models.ForeignKey(Nivel3, null=True, blank=True)

    codigo_cinema = models.CharField('Codigo Cinema', max_length=20, null=True, blank=True)
    grupo_ancine = models.ForeignKey(GrupoAncine, null=True, blank=True)
    numero_salas = models.IntegerField('Numero de Salas', null=True, blank=True)
    geom = models.GeometryField(null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nome




admin.site.register(Cinema)
