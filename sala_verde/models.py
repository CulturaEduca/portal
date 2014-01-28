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


class SalaVerde(models.Model):
    '''Modelagem nova Sala Verde'''

    id = models.IntegerField('ID', primary_key=True)
    longitude = models.FloatField('Longitude', null=True, blank=True)
    latitude = models.FloatField('Latitude', null=True, blank=True)
    tipogeo = models.ForeignKey(TipoGeo, null=True, blank=True)
    #ibge = models.IntegerField('IBGE', null=True, blank=True)
    ibge = models.ForeignKey(Municipio, db_column='ibge')
    nome = models.CharField('Nome', max_length=200, null=True, blank=True)
    endereco = models.CharField('Endereco', max_length=200, null=True, blank=True)
    cep = models.CharField('CEP', max_length=20, null=True, blank=True)
    ddd = models.CharField('DDD', max_length=3, null=True, blank=True)
    telefone1 = models.CharField('Telefone1', max_length=20, null=True, blank=True)
    telefone2 = models.CharField('Telefone2', max_length=20, null=True, blank=True)
    nome_responsavel = models.CharField('Nome do Responsavel', max_length=200, null=True, blank=True)
    email = models.CharField('Email', max_length=200, null=True, blank=True)
    email1 = models.CharField('Email1', max_length=200, null=True, blank=True)
    email2 = models.CharField('Email2', max_length=200, null=True, blank=True)
    instituicao = models.TextField('instituicao',  null=True, blank=True)
    infos = models.TextField('Infos', null=True, blank=True)
    geom = models.GeometryField(null=True, blank=True)
    objects = models.GeoManager()


    def __unicode__(self):
        return self.nome

admin.site.register(SalaVerde)