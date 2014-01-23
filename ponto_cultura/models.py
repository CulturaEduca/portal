# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.gis import admin
from django.contrib.gis.db import models
from ibge.models import Municipio


class TipoGeo(models.Model):
    '''Referencias do tipo Geo'''

    id = models.IntegerField('Cod TipoGEO', primary_key=True)
    nome = models.CharField('TipoGeo', null=True, blank=True, max_length=20)

    def __unicode__(self):
        return self.id

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

class TipoPonto(models.Model):
    '''Tipo do ponto de cultura'''

    nome = models.CharField('Tipo Ponto', max_length=100)

    def __unicode__(self):
        return self.nome


class PontoCultura(models.Model):
    '''Nova modelagem de pontos de cultura'''

    id = models.IntegerField('ID', primary_key=True)
    longitude = models.FloatField('Longitude', null=True, blank=True)
    latitude = models.FloatField('Latitude', null=True, blank=True)
    tipogeo = models.ForeignKey(TipoGeo, null=True, blank=True)
    ibge = models.IntegerField('IBGE', null=True, blank=True)
    num_controle_uf = models.IntegerField('Numero Controle UF', null=True, blank=True)
    #ibge = models.ForeignKey(Municipio, db_column='ibge')
    nome = models.CharField('Nome', max_length=200, null=True, blank=True)
    endereco = models.CharField('Endereco', max_length=200, null=True, blank=True)
    tipo_ponto = models.ForeignKey(TipoPonto, null=True, blank=True)
    projeto = models.CharField('Projeto', max_length=200, null=True, blank=True)
    entidade = models.CharField('Entidade', max_length=200, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=60, null=True, blank=True)
    endereco_original = models.CharField('Endereco Original', max_length=200, null=True, blank=True)
    cep = models.CharField('CEP', max_length=100, null=True, blank=True)
    tipo_logradouro = models.CharField('Tipo de Logradouro', max_length=100, null=True, blank=True)
    nome_logradouro = models.CharField('Endereco', max_length=300, null=True, blank=True)
    km = models.CharField('KM', max_length=200, null=True, blank=True)
    numero_logradouro = models.CharField('Numero', max_length=60, null=True, blank=True)
    complemento_logradouro = models.CharField('Complemento', max_length=200, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=300, null=True, blank=True)
    ddd_telefone1 = models.CharField('DDD Telefone', max_length=10, null=True, blank=True)
    ddd_telefone2 = models.CharField('DDD Telefone2', max_length=10, null=True, blank=True)
    ddd_telefone3 = models.CharField('DDD Telefone3', max_length=10, null=True, blank=True)
    ddd_telefone4 = models.CharField('DDD Telefone4', max_length=10, null=True, blank=True)
    ddd_telefone5 = models.CharField('DDD Telefone5', max_length=10, null=True, blank=True)
    ddd_telefone6 = models.CharField('DDD Telefone6', max_length=10, null=True, blank=True)
    telefone1 = models.CharField('Telefone1', max_length=10, null=True, blank=True)
    telefone2 = models.CharField('Telefone2', max_length=10, null=True, blank=True)
    telefone3 = models.CharField('Telefone3', max_length=10, null=True, blank=True)
    telefone4 = models.CharField('Telefone4', max_length=10, null=True, blank=True)
    telefone5 = models.CharField('Telefone5', max_length=10, null=True, blank=True)
    telefone6 = models.CharField('Telefone6', max_length=10, null=True, blank=True)
    fax = models.CharField('Fax', max_length=10, null=True, blank=True)
    blog = models.CharField('Blog', max_length=200, null=True, blank=True)
    site = models.CharField('Site', max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    email2 = models.EmailField(null=True, blank=True)
    email3 = models.EmailField(null=True, blank=True)
    email4 = models.EmailField(null=True, blank=True)
    email5 = models.EmailField(null=True, blank=True)
    responsavel = models.CharField('Responsavel', max_length=200, null=True, blank=True)
    publico_alvo = models.TextField('Publico Alvo', null=True, blank=True)
    atividades = models.TextField('Atividades', null=True, blank=True)
    processo = models.CharField('Processo', max_length=200, null=True, blank=True)
    numero_convenio = models.CharField('Numero do Convenio', max_length=200, null=True, blank=True)
    data_convenio = models.CharField('Data do Convenio', max_length=20, null=True, blank=True)
    edital = models.CharField('Edital', max_length=60, null=True, blank=True)
    vigencia_inicio = models.CharField('Vigencia Inicio', max_length=20, null=True, blank=True)
    vigencia_termino = models.CharField('Vigencia Termino', max_length=20, null=True, blank=True)
    parcela1 = models.CharField('Parcela 1', max_length=200, null=True, blank=True)
    parcela2 = models.CharField('Parcela 2', max_length=200, null=True, blank=True)
    parcela3 = models.CharField('Parcela 3', max_length=200, null=True, blank=True)
    parcela4 = models.CharField('Parcela 4', max_length=200, null=True, blank=True)
    parcela5 = models.CharField('Parcela 5', max_length=200, null=True, blank=True)
    contrapartida = models.CharField('Contrapartida', max_length=200, null=True, blank=True)
    valor_convenio = models.CharField('Valor Convenio', max_length=200, null=True, blank=True)
    geom = models.GeometryField(null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Ponto de Cultura'
        verbose_name_plural = 'Pontos de Cultura'

admin.site.register(PontoCultura)