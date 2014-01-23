from django.db import models

from ibge.models import Municipio

class BasicoPorMunicipio(models.Model):
    '''Nova modelagem basico por municipio'''

    cod_ibge = models.IntegerField(null=True, blank=True)
    v001 = models.IntegerField(null=True, blank=True)
    v002 = models.IntegerField(null=True, blank=True)
    num_setores = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.cod_ibge

    class Meta:
        verbose_name = 'Basico por Municipio'
        verbose_name_plural = 'Basicos por Municipio'


class BasicoPorSetor(models.Model):
    '''Nova modelagem basico por setor'''

    cod_ibge = models.IntegerField(null=True, blank=True)
    cod_setor = models.BigIntegerField(null=True, blank=True)
    situacao_setor = models.PositiveSmallIntegerField(null=True, blank=True)
    v001 = models.IntegerField(null=True, blank=True)
    v002 = models.IntegerField(null=True, blank=True)
    v003 = models.FloatField(null=True, blank=True)
    v004 = models.FloatField(null=True, blank=True)
    v005 = models.FloatField(null=True, blank=True)
    v006 = models.FloatField(null=True, blank=True)
    v007 = models.FloatField(null=True, blank=True)
    v008 = models.FloatField(null=True, blank=True)
    v009 = models.FloatField(null=True, blank=True)
    v010 = models.FloatField(null=True, blank=True)
    v011 = models.FloatField(null=True, blank=True)
    v012 = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.cod_ibge

    class Meta:
        verbose_name = 'Basico por Setor'
        verbose_name_plural = 'Basicos por Setor'
