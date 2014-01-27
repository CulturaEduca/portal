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

    nome = models.CharField('Tipo Esfera', max_length=100)

    def __unicode__(self):
        return self.nome

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
    longitude = models.FloatField('Longitude', null = True, blank = True)
    latitude = models.FloatField('Latitude', null = True, blank = True)
    tipogeo = models.ForeignKey(TipoGeo)
    ibge = models.ForeignKey(Municipio, null=True, blank=True, db_column='ibge')
    # ibge = models.IntegerField('IBGE', null=True, blank=True)
    nome = models.CharField('Nome da Biblioteca', max_length=200, null=True, blank=True)
    endereco_original = models.CharField('Endereco Original', max_length=200, null=True, blank=True)
    numero_original = models.CharField('Numero Original', max_length=200, null=True, blank=True)
    complemento_original = models.CharField('Complemento Original', max_length=200, null=True, blank=True)
    bairro_original = models.CharField('Bairro Original', max_length=200, null=True, blank=True)
    cep_original = models.CharField('CEP Orignal', max_length=30, null=True, blank=True)
    tipo_logradouro = models.CharField('Tipo de Logradouro', max_length=20, null=True, blank=True)
    nome_logradouro = models.CharField('Endereco', max_length=100, null=True, blank=True)
    km = models.CharField('KM', max_length=20, null=True, blank=True)
    numero_logradouro = models.CharField('Numero', max_length=20, null=True, blank=True)
    complemento_logradouro = models.CharField('Complemento', max_length=200, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=100, null=True, blank=True)
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)
    nome_responsavel = models.CharField('Nome Responsavel', max_length=100, null=True, blank=True)
    ddd_telefone1 = models.CharField('DDD Telefone', max_length=3, null=True, blank=True)
    telefone1 = models.CharField('Telefone1', max_length=10, null=True, blank=True)
    ddd_fax = models.CharField('DDD Fax', max_length=3, null=True, blank=True)
    fax = models.CharField('FAX', max_length=10, null=True, blank=True)
    email = models.EmailField('Email', null=True, blank=True)
    site = models.CharField('Site', max_length=200, null=True, blank=True)
    esfera_administrativa = models.ForeignKey(EsferaAdministrativa, null=True, blank=True)
    tipo_esfera = models.ForeignKey(TipoEsfera, null=True, blank=True)
    cnpj = models.CharField('CNPJ', max_length=20, null=True, blank=True)
    sniic_n1 = models.CharField('SNIIC N1', max_length=10, null=True, blank=True)
    sniic_n2 = models.CharField('SNIIC N2', max_length=10, null=True, blank=True)
    sniic_n3 = models.CharField('SNIIC N3', max_length=10, null=True, blank=True)

    # Especifico dessa base
    cod_censo_fgv = models.CharField('Codigo Censo FGV', max_length=10, null=True, blank=True)
    dias_funcionamento = models.ManyToManyField('DiaFuncionamento', null=True, blank=True)
    periodo_funcionamento = models.ManyToManyField('PeriodoFuncionamento', null=True, blank=True)
    acesso_internet = models.BooleanField('Acesso a Internet')
    qtd_emprestimos = models.IntegerField('Quantidade de Emprestimos', null=True, blank=True)
    qtd_livros_acervo = models.IntegerField('Quantidade de livros', null=True, blank=True)
    geom = models.GeometryField(null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nome



class BibliotecaOLD(models.Model):
    gid = models.IntegerField(primary_key=True)
    id = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    longitude = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    latitude = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    longitude1 = models.FloatField(null=True, blank=True)
    latitude1 = models.FloatField(null=True, blank=True)
    cod_ibge = models.FloatField(null=True, blank=True)
    nome = models.CharField(max_length=83, blank=True)
    end_orig = models.CharField(max_length=49, blank=True)
    num_orig = models.CharField(max_length=5, blank=True)
    compl_orig = models.CharField(max_length=32, blank=True)
    bairr_orig = models.CharField(max_length=26, blank=True)
    cep_orig = models.CharField(max_length=9, blank=True)
    tipo_logra = models.CharField(max_length=4, blank=True)
    nome_logra = models.CharField(max_length=49, blank=True)
    km = models.CharField(max_length=5, blank=True)
    num = models.IntegerField(null=True, blank=True)
    complement = models.CharField(max_length=32, blank=True)
    bairro = models.CharField(max_length=26, blank=True)
    cep = models.FloatField(null=True, blank=True)
    nome_resp = models.CharField(max_length=56, blank=True)
    ddd_telefo = models.CharField(max_length=2, blank=True)
    telefone = models.CharField(max_length=9, blank=True)
    ddd_fax = models.CharField(max_length=2, blank=True)
    fax = models.CharField(max_length=9, blank=True)
    email = models.CharField(max_length=50, blank=True)
    site = models.CharField(max_length=45, blank=True)
    esfera_adm = models.CharField(max_length=1, blank=True)
    sniic_n1 = models.CharField(max_length=1, blank=True)
    sniic_n2 = models.CharField(max_length=3, blank=True)
    sniic_n3 = models.CharField(max_length=5, blank=True)
    orgao_resp = models.CharField(max_length=1, blank=True)
    segunda = models.IntegerField(null=True, blank=True)
    terca = models.IntegerField(null=True, blank=True)
    quarta = models.IntegerField(null=True, blank=True)
    quinta = models.IntegerField(null=True, blank=True)
    sexta = models.IntegerField(null=True, blank=True)
    sabado = models.IntegerField(null=True, blank=True)
    domingo = models.IntegerField(null=True, blank=True)
    manha = models.IntegerField(null=True, blank=True)
    tarde = models.IntegerField(null=True, blank=True)
    noite = models.IntegerField(null=True, blank=True)
    acesso_usu = models.CharField(max_length=3, blank=True)
    qt_emprest = models.CharField(max_length=12, blank=True)
    acervo_liv = models.CharField(max_length=12, blank=True)
    geom = models.GeometryField(null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nome

    class Meta:
        db_table = 'biblioteca'

class BibliotecaAdmin(admin.ModelAdmin):
    a = True
    # raw_id_fields = ('ibge',)

#admin.site.register(Biblioteca)
admin.site.register(TipoGeo)
admin.site.register(TipoEsfera)
admin.site.register(EsferaAdministrativa)
admin.site.register(DiaFuncionamento)
admin.site.register(PeriodoFuncionamento)
admin.site.register(Biblioteca, BibliotecaAdmin)
