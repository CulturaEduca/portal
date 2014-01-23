# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.gis import admin
from django.contrib.gis.db import models
from ibge.models import Municipio
import datetime

class TipoGeo(models.Model):
    '''Referencias do tipo Geo'''

    id = models.IntegerField('Cod TipoGEO', primary_key=True)
    nome = models.CharField('TipoGeo', null=True, blank=True, max_length=20)

    def __unicode__(self):
        return self.id

class Instrumento(models.Model):
    '''Instrumento'''

    nome = models.CharField('Nome Instrumento', max_length=200)

    def __unicode__(self):
        return self.nome

class Tipo(models.Model):
    '''Tipo'''

    nome = models.CharField('Nome Tipo', max_length=200)

    def __unicode__(self):
        return self.nome

class EsferaAdministrativa(models.Model):
    '''Esfera'''

    nome = models.CharField('Esfera Administrativa', max_length=200)

    def __unicode__(self):
        return self.nome


class AreaAtuacao(models.Model):
    '''MTM Areas Atuacao'''

    nome = models.CharField('Nome Area', max_length=200)

    def __unicode__(self):
        return self.nome


class PublicoAlvo(models.Model):
    '''MTM PublicoAlvo'''

    nome = models.CharField('Nome Publico Alvo', max_length=200)

    def __unicode__(self):
        return self.nome

class ManifestacaoLinguagem(models.Model):
    '''MTM Manifestacao Linguagem'''

    nome = models.CharField('Nome Manifestacao e Linguagens', max_length=200)

    def __unicode__(self):
        return self.nome

class Premio(models.Model):
    '''MTM Premios'''

    nome = models.CharField('Nome Premio', max_length=200)
    ano = models.IntegerField('Ano Premio', null=True, blank=True)

    def __unicode__(self):
        return (self.nome + '/' + str(self.ano))


class Proponente(models.Model):
    '''Instituicao proponente do Ponto de Cultura'''

    cnpj = models.CharField('CNPJ', max_length=18, unique=True)
    razao_social = models.CharField('Razao Social', max_length=200)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=200, null=True, blank=True)
    ano_fundacao = models.IntegerField('Ano de Fundacao', null=True, blank=True)
    cnae = models.CharField('CNAE', max_length=200, null=True, blank=True)
    responsavel = models.CharField('Nome do Responsavel', max_length=200, null=True)
    endereco_original = models.CharField('Endereco Original', max_length=200, null=True, blank=True)
    ibge = models.ForeignKey(Municipio, help_text='Cidade e Municipio, clique na lupa para buscar')
    cep = models.CharField('CEP', max_length=100, null=True, blank=True)
    tipo_logradouro = models.CharField('Tipo de Logradouro', max_length=100, null=True, blank=True)
    nome_logradouro = models.CharField('Endereco', max_length=300, null=True, blank=True)
    km = models.CharField('KM', max_length=200, null=True, blank=True)
    numero_logradouro = models.CharField('Numero', max_length=60, null=True, blank=True)
    complemento_logradouro = models.CharField('Complemento', max_length=200, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=300, null=True, blank=True)
    ddd_telefone1 = models.CharField('DDD Telefone', max_length=2, null=True, blank=True)
    ddd_telefone2 = models.CharField('DDD Telefone2', max_length=2, null=True, blank=True)
    ddd_telefone3 = models.CharField('DDD Telefone3', max_length=2, null=True, blank=True)
    telefone1 = models.CharField('Telefone1', max_length=10, null=True, blank=True)
    telefone2 = models.CharField('Telefone2', max_length=10, null=True, blank=True)
    telefone3 = models.CharField('Telefone3', max_length=10, null=True, blank=True)
    fax = models.CharField('Fax', max_length=10, null=True, blank=True)
    blog = models.URLField('Blog', max_length=200, null=True, blank=True, help_text='http://www.exemplo.com')
    site = models.URLField('Site', max_length=200, null=True, blank=True, help_text='http://www.exemplo.com')
    email1 = models.EmailField(null=True, blank=True)
    email2 = models.EmailField(null=True, blank=True)
    email3 = models.EmailField(null=True, blank=True)
    longitude = models.FloatField('Longitude', null = True, blank = True)
    latitude = models.FloatField('Latitude', null = True, blank = True)
    tipogeo = models.ForeignKey(TipoGeo, null=True, blank=True)
    latlong = models.PointField('Latitude/Longitude', null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return (self.razao_social + ' (' + self.cnpj + ')')



class ProponenteAdmin(admin.ModelAdmin):
    list_display = ('razao_social','nome_fantasia','cnpj','ibge',)
    search_fields = ('razao_social','nome_fantasia','cnpj',)
    raw_id_fields = ('ibge',)
    list_filter = ('ibge__estado','ibge__nome',)


class Ponto(models.Model):
    '''Ponto de cultura'''

    cnpj = models.ForeignKey(Proponente)
    codigo = models.IntegerField('Codigo do Ponto')
    nome = models.CharField('Nome do Ponto', max_length=200)
    responsavel = models.CharField('Nome do Responsavel', max_length=200, null=True)
    endereco_original = models.CharField('Endereco Original', max_length=200, null=True, blank=True)
    ibge = models.ForeignKey(Municipio, help_text='Cidade e Municipio, clique na lupa para buscar')
    cep = models.CharField('CEP', max_length=100, null=True, blank=True)
    tipo_logradouro = models.CharField('Tipo de Logradouro', max_length=100, null=True, blank=True)
    nome_logradouro = models.CharField('Endereco', max_length=300, null=True, blank=True)
    km = models.CharField('KM', max_length=200, null=True, blank=True)
    numero_logradouro = models.CharField('Numero', max_length=60, null=True, blank=True)
    complemento_logradouro = models.CharField('Complemento', max_length=200, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=300, null=True, blank=True)
    ddd_telefone1 = models.CharField('DDD Telefone', max_length=2, null=True, blank=True)
    ddd_telefone2 = models.CharField('DDD Telefone2', max_length=2, null=True, blank=True)
    ddd_telefone3 = models.CharField('DDD Telefone3', max_length=2, null=True, blank=True)
    telefone1 = models.CharField('Telefone1', max_length=10, null=True, blank=True)
    telefone2 = models.CharField('Telefone2', max_length=10, null=True, blank=True)
    telefone3 = models.CharField('Telefone3', max_length=10, null=True, blank=True)
    fax = models.CharField('Fax', max_length=10, null=True, blank=True)
    blog = models.URLField('Blog', max_length=200, null=True, blank=True, help_text='http://www.exemplo.com')
    site = models.URLField('Site', max_length=200, null=True, blank=True, help_text='http://www.exemplo.com')
    email1 = models.EmailField(null=True, blank=True)
    email2 = models.EmailField(null=True, blank=True)
    email3 = models.EmailField(null=True, blank=True)
    longitude = models.FloatField('Longitude', null = True, blank = True)
    latitude = models.FloatField('Latitude', null = True, blank = True)
    tipogeo = models.ForeignKey(TipoGeo, null=True, blank=True)
    latlong = models.PointField('Latitude/Longitude', null=True, blank=True)
    objects = models.GeoManager()
    instrumento = models.ForeignKey(Instrumento, null=True, blank=True)
    tipo = models.ForeignKey(Tipo, null=True, blank=True)
    esfera_administrativa = models.ForeignKey(EsferaAdministrativa, null=True, blank=True)
    edital = models.CharField('Edital', max_length=60, null=True, blank=True)
    processo = models.CharField('Processo', max_length=200, null=True, blank=True)
    numero_convenio = models.CharField('Numero do Convenio', max_length=200, null=True, blank=True)
    pronac = models.CharField('PRONAC', max_length=200, null=True, blank=True)
    vigencia_inicio = models.DateField('Vigencia Inicio', null=True, blank=True)
    vigencia_termino = models.DateField('Vigencia Termino', null=True, blank=True)
    valor_global = models.FloatField('Valor Global', null=True, blank=True)
    repasse = models.FloatField('Repasse', null=True, blank=True)
    contrapartida = models.FloatField('Contrapartida', null=True, blank=True)
    parcela1 = models.FloatField('Parcela 1', null=True, blank=True)
    parcela2 = models.FloatField('Parcela 2', null=True, blank=True)
    parcela3 = models.FloatField('Parcela 3', null=True, blank=True)
    parcela4 = models.FloatField('Parcela 4', null=True, blank=True)
    parcela5 = models.FloatField('Parcela 5', null=True, blank=True)
    area_atuacao = models.ManyToManyField(AreaAtuacao, null=True, blank=True)
    publico_alvo = models.ManyToManyField(PublicoAlvo, null=True, blank=True)
    manifestacao_linguagem = models.ManyToManyField(ManifestacaoLinguagem, null=True, blank=True)
    sintese = models.TextField('Sintese', null=True, blank=True)
    premios = models.ManyToManyField(Premio, null=True, blank=True)
    sniic1 = models.CharField('SNIIC 1', max_length=20, null=True, blank=True)
    sniic2 = models.CharField('SNIIC 2', max_length=20, null=True, blank=True)
    sniic3 = models.CharField('SNIIC 3', max_length=20, null=True, blank=True)

    def __unicode__(self):
        return self.nome



class PontoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    raw_id_fields = ('ibge',)
    list_filter = ('ibge__estado','ibge__nome',)


admin.site.register(Proponente, ProponenteAdmin)
admin.site.register(Ponto, PontoAdmin)
admin.site.register(TipoGeo)
admin.site.register(Instrumento)
admin.site.register(Tipo)
admin.site.register(EsferaAdministrativa)
admin.site.register(AreaAtuacao)
admin.site.register(PublicoAlvo)
admin.site.register(ManifestacaoLinguagem)
admin.site.register(Premio)