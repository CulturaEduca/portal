from django.contrib.gis.db import models
from django.contrib.gis import admin


class TipoGeo(models.Model):
    '''Classe do TipoGeo'''

    cod = models.IntegerField('Codigo TipoGeo', unique=True, primary_key=True)
    nome = models.CharField('Nome TipoGeo', max_length = 100)

    def __unicode__(self):
        return self.nome 

admin.site.register(TipoGeo)