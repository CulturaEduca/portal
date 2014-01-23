from django.contrib.gis.db import models
from django.contrib.gis import admin

class Tipologia(models.Model):
    '''Tipologias SNIIC'''

    cid = models.IntegerField('ID, segundo SNIIC', unique=True)
    tipologia = models.CharField('Tipologia', max_length=255)
    codigo = models.CharField('Codigo SNIIC', max_length=255)
    descricao = models.CharField('Descricao', max_length=255)
    c1 = models.IntegerField('C1', null=True, blank=True)
    c2 = models.IntegerField('C2', null=True, blank=True)
    c3 = models.IntegerField('C3', null=True, blank=True)

    def __unicode__(self):
        return self.descricao 


admin.site.register(Tipologia)