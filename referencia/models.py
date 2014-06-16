from django.db import models
from django.contrib import admin

class Esfera(models.Model):
    '''Esfera Administrativa'''

    nome = models.CharField('Nome Esfera', max_length=100)

    def __unicode__(self):
        return self.nome

class TipoEsfera(models.Model):
    '''Tipo Esfera Administrativa'''

    nome = models.CharField('Tipo Esfera', max_length=100)
    esfera = models.ForeignKey('Esfera', null=True, blank=True)

    def __unicode__(self):
        return self.nome

admin.site.register(Esfera)
admin.site.register(TipoEsfera)