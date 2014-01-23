from django.contrib.gis import admin
from django.contrib.gis.db import models

class Saude(models.Model):
    gid = models.IntegerField(primary_key=True)
    id = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    longitude = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    latitude = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    longitude1 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    latitude1 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    longitude2 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    latitude2 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    tipogeo = models.CharField(max_length=30, blank=True)
    cod_ibge = models.CharField(max_length=7, blank=True)
    nome_empre = models.CharField(max_length=159, blank=True)
    nome = models.CharField(max_length=144, blank=True)
    end_orig = models.CharField(max_length=114, blank=True)
    num_orig = models.CharField(max_length=12, blank=True)
    bairr_orig = models.CharField(max_length=60, blank=True)
    cep_orig = models.IntegerField(null=True, blank=True)
    tipo_logra = models.CharField(max_length=30, blank=True)
    nome_logra = models.CharField(max_length=254, blank=True)
    km = models.CharField(max_length=30, blank=True)
    num_lograd = models.IntegerField(null=True, blank=True)
    complement = models.CharField(max_length=254, blank=True)
    bairro = models.CharField(max_length=60, blank=True)
    cep = models.CharField(max_length=9, blank=True)
    telefone = models.CharField(max_length=60, blank=True)
    esfera_adm = models.CharField(max_length=27, blank=True)
    tipo_esfer = models.CharField(max_length=30, blank=True)
    cnes_num = models.IntegerField(null=True, blank=True)
    cnes = models.CharField(max_length=21, blank=True)
    cod_link = models.CharField(max_length=39, blank=True)
    tipo_estab = models.CharField(max_length=150, blank=True)
    geom = models.GeometryField(null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nome

    class Meta:
        db_table = 'saude'
        verbose_name = 'Saude'
        verbose_name_plural = 'Saude'

admin.site.register(Saude)