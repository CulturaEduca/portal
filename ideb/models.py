# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.gis import admin
from django.contrib.gis.db import models

class Ciclo(models.Model):
    '''Ciclo Ideb'''

    nome = models.CharField('Ciclo', max_length=100)

    def __unicode__(self):
        return self.nome

class Ideb(models.Model):
    '''Classe IDEB'''

    codigo_inep = models.IntegerField('Codigo INEP')
    ciclo = models.ForeignKey(Ciclo, null=True, blank=True)
    i_fluxo_2005 = models.FloatField(null=True, blank=True)
    i_fluxo_2007 = models.FloatField(null=True, blank=True)
    i_fluxo_2009 = models.FloatField(null=True, blank=True)
    i_fluxo_2011 = models.FloatField(null=True, blank=True)
    i_matematica_2005 = models.FloatField(null=True, blank=True)
    i_portugues_2005 = models.FloatField(null=True, blank=True)
    i_nota_media_2005 = models.FloatField(null=True, blank=True)
    i_matematica_2007 = models.FloatField(null=True, blank=True)
    i_portugues_2007 = models.FloatField(null=True, blank=True)
    i_nota_media_2007 = models.FloatField(null=True, blank=True)
    i_matematica_2009 = models.FloatField(null=True, blank=True)
    i_portugues_2009 = models.FloatField(null=True, blank=True)
    i_nota_media_2009 = models.FloatField(null=True, blank=True)
    i_matematica_2011 = models.FloatField(null=True, blank=True)
    i_portugues_2011 = models.FloatField(null=True, blank=True)
    i_nota_media_201 = models.FloatField(null=True, blank=True)
    i_IDEB_2005 = models.FloatField(null=True, blank=True)
    i_IDEB_2007 = models.FloatField(null=True, blank=True)
    i_IDEB_2009 = models.FloatField(null=True, blank=True)
    i_IDEB_2011 = models.FloatField(null=True, blank=True)
    i_projecao_2007 = models.FloatField(null=True, blank=True)
    i_projecao_2009 = models.FloatField(null=True, blank=True)
    i_projecao_2011 = models.FloatField(null=True, blank=True)
    i_projecao_2013 = models.FloatField(null=True, blank=True)
    i_projecao_2015 = models.FloatField(null=True, blank=True)
    i_projecao_2017 = models.FloatField(null=True, blank=True)
    i_projecao_2019 = models.FloatField(null=True, blank=True)
    i_projecao_2021 = models.FloatField(null=True, blank=True)
    f_fluxo_2005 = models.FloatField(null=True, blank=True)
    f_fluxo_2007 = models.FloatField(null=True, blank=True)
    f_fluxo_2009 = models.FloatField(null=True, blank=True)
    f_fluxo_2011 = models.FloatField(null=True, blank=True)
    f_matematica_2005 = models.FloatField(null=True, blank=True)
    f_portugues_2005 = models.FloatField(null=True, blank=True)
    f_nota_media_2005 = models.FloatField(null=True, blank=True)
    f_matematica_2007 = models.FloatField(null=True, blank=True)
    f_portugues_2007 = models.FloatField(null=True, blank=True)
    f_nota_media_2007 = models.FloatField(null=True, blank=True)
    f_matematica_2009 = models.FloatField(null=True, blank=True)
    f_portugues_2009 = models.FloatField(null=True, blank=True)
    f_nota_media_2009 = models.FloatField(null=True, blank=True)
    f_matematica_2011 = models.FloatField(null=True, blank=True)
    f_portugues_2011 = models.FloatField(null=True, blank=True)
    f_nota_media_201 = models.FloatField(null=True, blank=True)
    f_IDEB_2005 = models.FloatField(null=True, blank=True)
    f_IDEB_2007 = models.FloatField(null=True, blank=True)
    f_IDEB_2009 = models.FloatField(null=True, blank=True)
    f_IDEB_2011 = models.FloatField(null=True, blank=True)
    f_projecao_2007 = models.FloatField(null=True, blank=True)
    f_projecao_2009 = models.FloatField(null=True, blank=True)
    f_projecao_2011 = models.FloatField(null=True, blank=True)
    f_projecao_2013 = models.FloatField(null=True, blank=True)
    f_projecao_2015 = models.FloatField(null=True, blank=True)
    f_projecao_2017 = models.FloatField(null=True, blank=True)
    f_projecao_2019 = models.FloatField(null=True, blank=True)
    f_projecao_2021 = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.codigo_inep)

admin.site.register(Ideb)
admin.site.register(Ciclo)