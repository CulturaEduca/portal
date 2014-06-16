# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EsferaAdministrativa'
        db.create_table(u'teatro_esferaadministrativa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'teatro', ['EsferaAdministrativa'])

        # Adding model 'TipoEsfera'
        db.create_table(u'teatro_tipoesfera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'teatro', ['TipoEsfera'])

        # Adding model 'Teatro'
        db.create_table(u'teatro_teatro', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('codigo_teatro', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('tipogeo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorio.TipoGeo'])),
            ('ibge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ibge.Municipio'], db_column=u'ibge')),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('codigo_original', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('endereco_original', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('bairro_original', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('cep_original', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('tipo_logradouro', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('nome_logradouro', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('km', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('numero_logradouro', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('complemento_logradouro', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('ddd_telefone1', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('telefone1', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('telefone2', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('esfera_administrativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teatro.EsferaAdministrativa'], null=True, blank=True)),
            ('tipo_esfera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teatro.TipoEsfera'], null=True, blank=True)),
            ('cnpj', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('sniic_n1', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('sniic_n2', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('sniic_n3', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('cod_adm', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('numero_lugares', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('data_inaugacao', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('ano_inauguracao', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ano_desaparecimento', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('historia_espaco', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fonte_original', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('data_info', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.GeometryField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'teatro', ['Teatro'])


    def backwards(self, orm):
        # Deleting model 'EsferaAdministrativa'
        db.delete_table(u'teatro_esferaadministrativa')

        # Deleting model 'TipoEsfera'
        db.delete_table(u'teatro_tipoesfera')

        # Deleting model 'Teatro'
        db.delete_table(u'teatro_teatro')


    models = {
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
        u'teatro.esferaadministrativa': {
            'Meta': {'object_name': 'EsferaAdministrativa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'teatro.teatro': {
            'Meta': {'object_name': 'Teatro'},
            'ano_desaparecimento': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ano_inauguracao': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'bairro_original': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'cep_original': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cod_adm': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'codigo_original': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'codigo_teatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'complemento_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'data_inaugacao': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'data_info': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ddd_telefone1': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'endereco_original': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'esfera_administrativa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teatro.EsferaAdministrativa']", 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'fonte_original': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True', 'blank': 'True'}),
            'historia_espaco': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ibge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ibge.Municipio']", 'db_column': "u'ibge'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'km': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nome_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'numero_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'numero_lugares': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sniic_n1': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sniic_n2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sniic_n3': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone1': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tipo_esfera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teatro.TipoEsfera']", 'null': 'True', 'blank': 'True'}),
            'tipo_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tipogeo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['territorio.TipoGeo']"})
        },
        u'teatro.tipoesfera': {
            'Meta': {'object_name': 'TipoEsfera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'territorio.tipogeo': {
            'Meta': {'object_name': 'TipoGeo'},
            'cod': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['teatro']