# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EsferaAdministrativa'
        db.create_table(u'cinema_esferaadministrativa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'cinema', ['EsferaAdministrativa'])

        # Adding model 'TipoEsfera'
        db.create_table(u'cinema_tipoesfera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'cinema', ['TipoEsfera'])

        # Adding model 'GrupoAncine'
        db.create_table(u'cinema_grupoancine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'cinema', ['GrupoAncine'])

        # Adding model 'Cinema'
        db.create_table(u'cinema_cinema', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('tipogeo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorio.TipoGeo'])),
            ('ibge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ibge.Municipio'], null=True, db_column=u'ibge', blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('endereco_original', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('numero_original', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('complemento_original', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('bairro_original', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('cep_original', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('tipo_logradouro', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('nome_logradouro', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('km', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('numero_logradouro', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('complemento_logradouro', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('nome_responsavel', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ddd', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('telefone1', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('telefone2', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('telefone3', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('esfera_administrativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cinema.EsferaAdministrativa'], null=True, blank=True)),
            ('tipo_esfera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cinema.TipoEsfera'], null=True, blank=True)),
            ('cnpj', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('sniic_n1', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('sniic_n2', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('sniic_n3', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('grupo_ancine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cinema.GrupoAncine'], null=True, blank=True)),
            ('numero_salas', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.GeometryField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'cinema', ['Cinema'])


    def backwards(self, orm):
        # Deleting model 'EsferaAdministrativa'
        db.delete_table(u'cinema_esferaadministrativa')

        # Deleting model 'TipoEsfera'
        db.delete_table(u'cinema_tipoesfera')

        # Deleting model 'GrupoAncine'
        db.delete_table(u'cinema_grupoancine')

        # Deleting model 'Cinema'
        db.delete_table(u'cinema_cinema')


    models = {
        u'cinema.cinema': {
            'Meta': {'object_name': 'Cinema'},
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'bairro_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'cep_original': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'complemento_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'complemento_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ddd': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'endereco_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'esfera_administrativa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cinema.EsferaAdministrativa']", 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True', 'blank': 'True'}),
            'grupo_ancine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cinema.GrupoAncine']", 'null': 'True', 'blank': 'True'}),
            'ibge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ibge.Municipio']", 'null': 'True', 'db_column': "u'ibge'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'km': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'nome_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'nome_responsavel': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'numero_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'numero_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'numero_salas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'sniic_n1': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sniic_n2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sniic_n3': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone1': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone3': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tipo_esfera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cinema.TipoEsfera']", 'null': 'True', 'blank': 'True'}),
            'tipo_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tipogeo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['territorio.TipoGeo']"})
        },
        u'cinema.esferaadministrativa': {
            'Meta': {'object_name': 'EsferaAdministrativa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cinema.grupoancine': {
            'Meta': {'object_name': 'GrupoAncine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'cinema.tipoesfera': {
            'Meta': {'object_name': 'TipoEsfera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'ibge.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'area': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'cd_geocodm': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'codigo_ibge': ('django.db.models.fields.IntegerField', [], {}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ibge.Uf']", 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'raio': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'ibge.uf': {
            'Meta': {'object_name': 'Uf'},
            'area': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'codigo_ibge': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'territorio.tipogeo': {
            'Meta': {'object_name': 'TipoGeo'},
            'cod': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cinema']