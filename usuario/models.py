# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from django.contrib.gis import admin
from ibge.models import Municipio

class Sexo(models.Model):
    '''Sexo'''

    nome = models.CharField(u'Sexo', max_length=20)
    abbr = models.CharField(u'Abreviado', max_length=3)

    def __unicode__(self):
        return self.nome

class Etnia(models.Model):
    '''Etnias'''

    nome = models.CharField(u'Etnia', max_length=100)

    def __unicode__(self):
        return self.nome

class Usuario(models.Model):
    '''Classe de usuarios'''

    email = models.EmailField(u'E-Mail', unique=True)
    nome = models.CharField(u'Nome', max_length=100)
    sobrenome = models.CharField(u'Sobrenome', max_length=200)
    senha = models.CharField(u'Senha', max_length=300)
    sexo = models.ForeignKey('Sexo', null=True, blank=True)
    data_nascimento = models.DateField(u'Data de Nascimento', null=True, blank=True)
    etnia = models.ForeignKey('Etnia', null=True, blank=True)
    cpf = models.CharField(u'CPF', max_length=100, null=True, blank=True)
    cep = models.CharField(u'CEP', max_length=20, null=True, blank=True)
    nome_logradouro = models.CharField(u'Nome do Logradouro', max_length=200, null=True, blank=True)
    numero_logradouro = models.CharField(u'Número Logradouro', max_length=20, null=True, blank=True)
    complemento = models.CharField(u'Complemento', max_length=100, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, blank=True, null=True)
    chave = models.CharField(u'Chave autenticação', max_length=260, null=True, blank=True)
    ativo = models.BooleanField(u'Usuário Ativo')
    verificado = models.BooleanField(u'Usuário Verificado')
    latitude = models.FloatField(u'Latitude', null=True, blank=True)
    longitude = models.FloatField(u'Longitude', null=True, blank=True)
    latlong = models.PointField('Latitude/Longitude', null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class UsuarioAdmin(admin.ModelAdmin):
    raw_id_fields = ('municipio',)

admin.site.register(Sexo)
admin.site.register(Etnia)
admin.site.register(Usuario, UsuarioAdmin)