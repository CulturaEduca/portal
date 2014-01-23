# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.gis import admin
from django.contrib.gis.db import models
from ibge.models import Municipio

class Macrocampo(models.Model):
    '''Macrocampos'''

    nome = models.CharField('Macrocampo', max_length=200)
    nome_curto = models.CharField('Nome Curto', max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Macrocampo'
        verbose_name_plural = 'Macrocampos'

class Atividade(models.Model):
    '''Atividades'''

    nome = models.CharField('Nome da Atividade', max_length=200)
    nome_curto = models.CharField('Nome curto', max_length=200, null=True, blank=True)
    macrocampo = models.ForeignKey('Macrocampo', null=True, blank=True)

    def __unicode__(self):
        return ('%s/%s' % (self.macrocampo, self.nome))

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

class Regiao(models.Model):
    '''Regiões administrativas'''

    nome = models.CharField(u'Região', max_length=100)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Região'
        verbose_name_plural = 'Regiões'


class Localizacao(models.Model):
    '''Localização da escola'''

    nome = models.CharField(u'Localização', max_length=100)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'


class DepAdm(models.Model):
    '''Dependência Administrativa'''

    nome = models.CharField(u'Dependência Administrativa', max_length=100)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Dependência Administrativa'
        verbose_name_plural = 'Dependências Administrativas'


class Situacao(models.Model):
    '''Situação da escolas'''

    nome = models.CharField(u'Situação', max_length=100)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Situação da Escola'
        verbose_name_plural = 'Situações das Escolas'

class Programa(models.Model):
    '''Programas'''

    nome = models.CharField(u'Programa', max_length=100)

    def __unicode__(self):
        return self.nome 

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

class Atributo(models.Model):
    '''Atributos'''

    nome = models.CharField(u'Atributos', max_length=100)

    def __unicode__(self):
        return self.nome 

    class Meta:
        verbose_name = 'Atributo'
        verbose_name_plural = 'Atributos'


class Escola(models.Model):
    '''Escolas'''

    codigo_inep = models.IntegerField(u'Código INEP', unique=True)
    ibge = models.ForeignKey(Municipio)
    nome = models.CharField(u'Nome Escola', max_length=200)
    regiao = models.ForeignKey('Regiao', null=True, blank=True, verbose_name='Região')
    localizacao = models.ForeignKey('Localizacao', null=True, blank=True, verbose_name='Localização')
    dep_adm = models.ForeignKey('DepAdm', null=True, blank=True, verbose_name='Dependência Administrativa')
    nome_diretor = models.CharField(u'Nome do Diretor', max_length=200, null=True, blank=True)
    telefone_diretor = models.CharField(u'Telefone do Diretor', max_length=100, null=True, blank=True)
    email_diretor = models.CharField(u'Email do Diretor', max_length=100, null=True, blank=True)
    latitude = models.FloatField(u'Latitude', null=True, blank=True)
    longitude = models.FloatField(u'Longitude', null=True, blank=True)
    tipo_logradouro = models.CharField(u'Tipo de Logradouro', max_length=20, null=True, blank=True)
    nome_logradouro = models.CharField(u'Endereço', max_length=200, null=True, blank=True)
    numero_logradouro = models.CharField(u'Número do Logradouro', max_length=100, null=True, blank=True)
    complemento = models.CharField(u'Complemento', max_length=100, null=True, blank=True)
    bairro = models.CharField(u'Bairro', max_length=100, null=True, blank=True)
    cep = models.CharField(u'CEP', max_length=20, null=True, blank=True)
    ddd = models.CharField(u'DDD', max_length=10, null=True, blank=True)
    tel1 = models.CharField(u'Telefone 1', max_length=50, null=True, blank=True)
    tel2 = models.CharField(u'Telefone 2', max_length=50, null=True, blank=True)
    fax = models.CharField(u'FAX', max_length=50, null=True, blank=True)
    email = models.CharField(u'Email', max_length=200, null=True, blank=True)
    situacao = models.ForeignKey('Situacao', null=True, blank=True)
    total_alunos = models.IntegerField(u'Total de Alunos', null=True, blank=True)
    atributos = models.ManyToManyField('Atributo', null=True, blank=True)
    programas = models.ManyToManyField('Programa', null=True, blank=True)
    atividades = models.ManyToManyField('Atividade', null=True, blank=True)
    latlong = models.PointField('Latitude/Longitude', null=True, blank=True)
    raio_territorio = models.FloatField('Raio do Territorio', null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'

class DadosEscolas(models.Model):
    id = models.IntegerField(primary_key=True)
    cod_inep = models.CharField(max_length=8, blank=True)
    cod_ibge = models.CharField(max_length=7, blank=True)
    id_sala_diretoria = models.IntegerField(null=True, blank=True)
    id_sala_professor = models.IntegerField(null=True, blank=True)
    id_laboratorio_informatica = models.IntegerField(null=True, blank=True)
    id_laboratorio_ciencias = models.IntegerField(null=True, blank=True)
    id_sala_atendimento_especial = models.IntegerField(null=True, blank=True)
    id_quadra_esportes_coberta = models.IntegerField(null=True, blank=True)
    id_quadra_esportes_descoberta = models.IntegerField(null=True, blank=True)
    id_cozinha = models.IntegerField(null=True, blank=True)
    id_biblioteca = models.IntegerField(null=True, blank=True)
    id_sala_leitura = models.IntegerField(null=True, blank=True)
    id_sanitario_fora_predio = models.IntegerField(null=True, blank=True)
    id_sanitario_dentro_predio = models.IntegerField(null=True, blank=True)
    id_dependencias_pne = models.IntegerField(null=True, blank=True)
    id_auditorio = models.IntegerField(null=True, blank=True)
    id_patio_coberto = models.IntegerField(null=True, blank=True)
    id_patio_descoberto = models.IntegerField(null=True, blank=True)
    id_area_verde = models.IntegerField(null=True, blank=True)
    num_salas_existentes = models.IntegerField(null=True, blank=True)
    num_salas_utilizadas = models.IntegerField(null=True, blank=True)
    id_equip_tv = models.IntegerField(null=True, blank=True)
    id_equip_dvd = models.IntegerField(null=True, blank=True)
    id_equip_copiadora = models.IntegerField(null=True, blank=True)
    id_equip_impressora = models.IntegerField(null=True, blank=True)
    id_equip_som = models.IntegerField(null=True, blank=True)
    id_equip_multimidia = models.IntegerField(null=True, blank=True)
    id_equip_foto = models.IntegerField(null=True, blank=True)
    id_computadores = models.IntegerField(null=True, blank=True)
    num_computadores = models.IntegerField(null=True, blank=True)
    num_comp_administrativos = models.IntegerField(null=True, blank=True)
    num_comp_alunos = models.IntegerField(null=True, blank=True)
    id_internet = models.IntegerField(null=True, blank=True)
    id_banda_larga = models.IntegerField(null=True, blank=True)
    num_funcionarios = models.IntegerField(null=True, blank=True)
    id_alimentacao = models.IntegerField(null=True, blank=True)
    id_aee = models.IntegerField(null=True, blank=True)
    id_mod_ens_esp = models.IntegerField(null=True, blank=True)
    id_mod_ativ_complementar = models.IntegerField(null=True, blank=True)
    id_mod_ens_regular = models.IntegerField(null=True, blank=True)
    id_mod_eja = models.IntegerField(null=True, blank=True)
    id_reg_infantil_creche = models.IntegerField(null=True, blank=True)
    id_reg_infantil_preescola = models.IntegerField(null=True, blank=True)
    id_reg_fund_8_anos = models.IntegerField(null=True, blank=True)
    id_reg_fund_9_anos = models.IntegerField(null=True, blank=True)
    id_reg_medio_medio = models.IntegerField(null=True, blank=True)
    id_reg_medio_integrado = models.IntegerField(null=True, blank=True)
    id_reg_medio_normal = models.IntegerField(null=True, blank=True)
    id_reg_medio_prof = models.IntegerField(null=True, blank=True)
    id_eja_fundamental = models.IntegerField(null=True, blank=True)
    id_eja_medio = models.IntegerField(null=True, blank=True)
    id_eja_projovem = models.IntegerField(null=True, blank=True)
    id_localizacao_diferenciada = models.IntegerField(null=True, blank=True)
    id_material_esp_quilombola = models.IntegerField(null=True, blank=True)
    id_material_esp_indigena = models.IntegerField(null=True, blank=True)
    id_educacao_indigena = models.IntegerField(null=True, blank=True)
    id_abre_final_semana = models.IntegerField(null=True, blank=True)
    prog_mais_educacao = models.IntegerField(null=True, blank=True)
    num_alunos_mais_educacao = models.IntegerField(null=True, blank=True)
    prog_em_inovador = models.IntegerField(null=True, blank=True)
    prog_escola_aberta = models.IntegerField(null=True, blank=True)
    prog_pse = models.IntegerField(null=True, blank=True)
    num_alunos_pse = models.IntegerField(null=True, blank=True)
    prog_pba = models.IntegerField(null=True, blank=True)
    coordenador_mais_educacao = models.CharField(max_length=55, blank=True)
    cpfcoordenador_mais_educacao = models.CharField(max_length=11, blank=True)
    emailcoordenador_mais_educacao = models.CharField(max_length=55, blank=True)
    telefonecoordenador_mais_educacao = models.CharField(max_length=14, blank=True)
    celularcoordenador_mais_educacao = models.CharField(max_length=15, blank=True)
    recursosfnde = models.CharField(max_length=1, blank=True)
    recursopago = models.CharField(max_length=9, blank=True)
    brasilsemmiseria = models.CharField(max_length=1, blank=True)

    def __unicode__(self):
        return self.cod_inep

    class Meta:
        db_table = 'dados_escolas'
        verbose_name = 'Dado Escolar'
        verbose_name_plural = 'Dados Escolares'


class EscolaAdmin(admin.ModelAdmin):
    '''Admin Escolas'''

    list_display = ('nome','codigo_inep','nome_logradouro','numero_logradouro','cep','ibge','latitude','longitude','raio_territorio',)
    search_fields = ('nome','codigo_inep','ibge__nome',)
    raw_id_fields = ('ibge',)
    list_filter = ('ibge__estado','ibge__nome','programas','atividades',)

admin.site.register(Escola, EscolaAdmin)
admin.site.register(Macrocampo)
admin.site.register(Atividade)
admin.site.register(Regiao)
admin.site.register(Localizacao)
admin.site.register(DepAdm)
admin.site.register(Situacao)
admin.site.register(Atributo)
admin.site.register(Programa)
admin.site.register(DadosEscolas)