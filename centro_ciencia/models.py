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


class CentroCiencia(models.Model):
    '''Nova modelagem de Centro de Ciencia'''

    id = models.IntegerField(primary_key=True)
    longitude = models.FloatField('Longitude', null = True, blank = True)
    latitude = models.FloatField('Latitude', null = True, blank = True)
    tipogeo = models.ForeignKey(TipoGeo)
    ibge = models.ForeignKey(Municipio, db_column='ibge')
    #ibge = models.IntegerField('IBGE', null=True, blank=True)
    nome = models.CharField('Nome da Biblioteca', max_length=300, null=True, blank=True)
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
    ddd = models.CharField('DDD Telefone', max_length=3, null=True, blank=True)
    telefone1 = models.CharField('Telefone1', max_length=10, null=True, blank=True)
    telefone2 = models.CharField('Telefone2', max_length=10, null=True, blank=True)
    telefone3 = models.CharField('Telefone3', max_length=10, null=True, blank=True)
    site = models.CharField('Site', max_length=300, null=True, blank=True)
    email = models.CharField('Email', max_length=200, null=True, blank=True)
    esfera_administrativa = models.ForeignKey(EsferaAdministrativa, null=True, blank=True)
    tipo_esfera = models.ForeignKey(TipoEsfera, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=200, null=True, blank=True)
    sniic_n1 = models.CharField('SNIIC N1', max_length=10, null=True, blank=True)
    sniic_n2 = models.CharField('SNIIC N2', max_length=10, null=True, blank=True)
    sniic_n3 = models.CharField('SNIIC N3', max_length=10, null=True, blank=True)
    geom = models.GeometryField(null=True, blank=True)
    objects = models.GeoManager()


    def __unicode__(self):
        return self.nome


class CentrosDeCiencia(models.Model):
    gid = models.IntegerField(primary_key=True)
    id = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    longitude = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    latitude = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    longitude1 = models.FloatField(null=True, blank=True)
    latitude1 = models.FloatField(null=True, blank=True)
    longitude2 = models.FloatField(null=True, blank=True)
    latitude2 = models.FloatField(null=True, blank=True)
    tipogeo = models.CharField(max_length=28, blank=True)
    uf = models.CharField(max_length=2, blank=True)
    municipio = models.CharField(max_length=24, blank=True)
    cod_ibge = models.CharField(max_length=7, blank=True)
    nome = models.CharField(max_length=78, blank=True)
    end_orig = models.CharField(max_length=38, blank=True)
    num_orig = models.CharField(max_length=8, blank=True)
    compl_orig = models.CharField(max_length=70, blank=True)
    bairr_orig = models.CharField(max_length=41, blank=True)
    cep_orig = models.CharField(max_length=9, blank=True)
    tipo_logra = models.CharField(max_length=4, blank=True)
    nome_logra = models.CharField(max_length=38, blank=True)
    km_logrado = models.CharField(max_length=6, blank=True)
    num_lograd = models.FloatField(null=True, blank=True)
    complement = models.CharField(max_length=59, blank=True)
    bairro = models.CharField(max_length=41, blank=True)
    cep = models.CharField(max_length=9, blank=True)
    esfera_adm = models.CharField(max_length=1, blank=True)
    tipo_esfer = models.CharField(max_length=1, blank=True)
    ddd = models.IntegerField(null=True, blank=True)
    telefone1 = models.CharField(max_length=9, blank=True)
    telefone2 = models.CharField(max_length=9, blank=True)
    email = models.CharField(max_length=47, blank=True)
    site = models.CharField(max_length=59, blank=True)
    geom = models.GeometryField(null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nome

    class Meta:
        db_table = 'centros_de_ciencia'
        verbose_name = 'Centro de Ciencia'
        verbose_name_plural = 'Centros de Ciencia'

admin.site.register(CentroCiencia)