# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Biblioteca.tipologia_sniic'
        db.add_column(u'biblioteca_biblioteca', 'tipologia_sniic',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sniic.Nivel3'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Biblioteca.tipologia_sniic'
        db.delete_column(u'biblioteca_biblioteca', 'tipologia_sniic_id')


    models = {
        u'biblioteca.biblioteca': {
            'Meta': {'object_name': 'Biblioteca'},
            'acervo_livros': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'acesso_usuario_internet': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bairro_original': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'cep_original': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cnpj_mantenedor': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cod_censo_fgv': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'codigo_biblioteca': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'codigo_equipamento': ('django.db.models.fields.IntegerField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'complemento_original': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ddd_fax': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ddd_telefone1': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ddd_telefone2': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ddd_telefone3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'dias_funcionamento': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['biblioteca.DiaFuncionamento']", 'null': 'True', 'blank': 'True'}),
            'email1': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email2': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email3': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'endereco_original': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True', 'blank': 'True'}),
            'ibge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ibge.Municipio']", 'null': 'True', 'db_column': "u'ibge'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'km': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mantenedor': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nome_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nome_responsavel': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'numero_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'numero_original': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'periodo_funcionamento': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['biblioteca.PeriodoFuncionamento']", 'null': 'True', 'blank': 'True'}),
            'qtd_emprestimos_domiciliar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sniic_n1': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sniic_n2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sniic_n3': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone1': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone3': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tipo_esfera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['referencia.TipoEsfera']", 'null': 'True', 'blank': 'True'}),
            'tipo_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tipogeo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['territorio.TipoGeo']"}),
            'tipologia_sniic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sniic.Nivel3']", 'null': 'True', 'blank': 'True'})
        },
        u'biblioteca.diafuncionamento': {
            'Meta': {'object_name': 'DiaFuncionamento'},
            'dia': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'biblioteca.periodofuncionamento': {
            'Meta': {'object_name': 'PeriodoFuncionamento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'periodo': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
        u'referencia.esfera': {
            'Meta': {'object_name': 'Esfera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'referencia.tipoesfera': {
            'Meta': {'object_name': 'TipoEsfera'},
            'esfera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['referencia.Esfera']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sniic.nivel1': {
            'Meta': {'object_name': 'Nivel1'},
            'cod': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'sniic.nivel2': {
            'Meta': {'object_name': 'Nivel2'},
            'cod': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel1': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sniic.Nivel1']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'sniic.nivel3': {
            'Meta': {'object_name': 'Nivel3'},
            'cod': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel1': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sniic.Nivel1']"}),
            'nivel2': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sniic.Nivel2']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'territorio.tipogeo': {
            'Meta': {'object_name': 'TipoGeo'},
            'cod': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['biblioteca']