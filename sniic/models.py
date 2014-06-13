from django.contrib.gis.db import models
from django.contrib.gis import admin

class Tipologia(models.Model):
    '''Tipologias SNIIC'''

    cid = models.IntegerField('ID, segundo SNIIC', unique = True)
    tipologia = models.CharField('Tipologia', max_length = 255)
    codigo = models.CharField('Codigo SNIIC', max_length = 255)
    descricao = models.CharField('Descricao', max_length = 255)
    c1 = models.IntegerField('C1', null = True, blank = True)
    c2 = models.IntegerField('C2', null = True, blank = True)
    c3 = models.IntegerField('C3', null = True, blank = True)

    def __unicode__(self):
        return self.descricao 

class Nivel1(models.Model):
    '''Primeiro nivel da tipologia SNIIC'''

    cod = models.IntegerField('Codigo nivel 1 SNIIC')
    titulo = models.CharField('Titulo nivel 1', max_length = 200)

    def __unicode__(self):
        return str(self.cod) + '-' + self.titulo 


class Nivel2(models.Model):
    '''Segundo nivel da tipologia SNIIC'''

    cod = models.IntegerField('Codigo nivel 2 SNIIC')
    nivel1 = models.ForeignKey('Nivel1')
    titulo = models.CharField('Titulo nivel 2', max_length = 200)

    def __unicode__(self):
        return str(self.cod) + '-' + self.titulo

class Nivel3(models.Model):
    '''Terceiro nivel da tipologia SNIIC'''

    cod = models.IntegerField('Codigo nivel 3 SNIIC')
    nivel1 = models.ForeignKey('Nivel1')
    nivel2 = models.ForeignKey('Nivel2')
    titulo = models.CharField('Titulo nivel 3', max_length = 200)

    def __unicode__(self):
        return str(self.cod) + '-' + self.titulo


class TipologiaAdmin(admin.ModelAdmin):
    list_display = ('codigo','descricao','tipologia',)



admin.site.register(Tipologia, TipologiaAdmin)
admin.site.register(Nivel1)
admin.site.register(Nivel2)
admin.site.register(Nivel3)