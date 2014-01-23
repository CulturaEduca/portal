# -*- coding: utf-8 -*-

from django.contrib.gis import admin
from django.contrib.gis.db import models

class Uf(models.Model):
    '''Classe dos Estados'''

    codigo_ibge = models.IntegerField('Codigo IBGE', unique=True)
    nome = models.CharField('Estado', max_length=50)
    sigla = models.CharField('Sigla', max_length=2)
    area = models.MultiPolygonField(null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.sigla

    class Meta:
        verbose_name = 'Unidade Federativa'
        verbose_name_plural = 'Unidades Federativas'


class Municipio(models.Model):
    '''Municipios'''

    codigo_ibge = models.IntegerField('Codigo Sistema')
    cd_geocodm = models.IntegerField('Codigo IBGE', unique=True, primary_key=True)
    nome = models.CharField('Municipio', max_length=60)
    estado = models.ForeignKey(Uf, null=True, blank=True)
    slug = models.CharField('Slug de busca do municipio', max_length=200, null=True, blank=True)
    raio = models.FloatField('Raio do Municipio', null=True, blank=True)
    area = models.MultiPolygonField()
    objects = models.GeoManager()

    def __unicode__(self):
        return "%s/%s" % (self.nome, self.estado)

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'


class MunicipioAdmin(admin.OSMGeoAdmin):
    list_display = ('nome','estado','cd_geocodm','slug','raio',)
    search_fields = ('nome',)


class Tipo(models.Model):
    '''Tipo de localidade'''

    nome = models.CharField('Tipo da localidade', max_length=20)

    def __unicode__(self):
        return self.nome

class SetorCensitario(models.Model):
    '''Setores censitarios'''

    codigo_ibge = models.IntegerField(null=True, blank=True)
    cd_geocodi = models.CharField(max_length=20, null=True, blank=True)
    tipo = models.CharField(max_length=10, null=True, blank=True)
    cd_geocodb = models.CharField(max_length=20, null=True, blank=True)
    nm_bairro = models.CharField(max_length=60, null=True, blank=True)
    cd_geocods = models.CharField(max_length=20, null=True, blank=True)
    nm_subdist = models.CharField(max_length=60, null=True, blank=True)
    cd_geocodd = models.CharField(max_length=20, null=True, blank=True)
    nm_distrit = models.CharField(max_length=60, null=True, blank=True)
    # cd_geocodm = models.IntegerField()
    cd_geocodm = models.ForeignKey(Municipio, db_column='cd_geocodm')
    nm_municip = models.CharField(max_length=60, null=True, blank=True)
    nm_micro = models.CharField(max_length=100, null=True, blank=True)
    nm_meso = models.CharField(max_length=100, null=True, blank=True)
    setor_censitario_bruto = models.MultiPolygonField(null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nm_municip

    class Meta:
        verbose_name = 'Setor Censitário'
        verbose_name_plural = 'Setores Censitários'


class SetorCensitarioAdmin(admin.OSMGeoAdmin):
    list_display = ('cd_geocodi','nm_bairro','nm_distrit','cd_geocodm','nm_micro','nm_meso',)
    raw_id_fields = ('cd_geocodm',)
    search_fields = ('nm_municip','nm_micro','nm_distrit','nm_bairro','cd_geocodi',)


class Domicilios(models.Model):
    '''Domicilios censitarios'''

    setor = models.CharField(max_length=20, null=True, blank=True)
    domicilios = models.IntegerField(null=True, blank=True)
    moradores = models.IntegerField(null=True, blank=True)
    rendimento = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    alf_mais_dez = 	models.IntegerField(null=True, blank=True)
    faixa_sete_dezoito = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.setor

    class Meta:
        verbose_name = 'Domicílio'
        verbose_name_plural = 'Domicílios'

class DomiciliosAdmin(admin.OSMGeoAdmin):
    list_display = ('setor','domicilios','moradores','rendimento','alf_mais_dez','faixa_sete_dezoito',)
    search_fields = ('setor',)


admin.site.register(SetorCensitario, SetorCensitarioAdmin)
admin.site.register(Uf, admin.GeoModelAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Tipo, admin.GeoModelAdmin)
admin.site.register(Domicilios, DomiciliosAdmin)
