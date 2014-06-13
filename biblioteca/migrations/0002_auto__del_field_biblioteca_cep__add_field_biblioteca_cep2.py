# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Biblioteca.cep'
        db.delete_column(u'biblioteca_biblioteca', 'cep')

        # Adding field 'Biblioteca.cep2'
        db.add_column(u'biblioteca_biblioteca', 'cep2',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Biblioteca.cep'
        db.add_column(u'biblioteca_biblioteca', 'cep',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Biblioteca.cep2'
        db.delete_column(u'biblioteca_biblioteca', 'cep2')


    models = {
        u'biblioteca.biblioteca': {
            'Meta': {'object_name': 'Biblioteca'},
            'acesso_internet': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bairro_original': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cep2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'cep_original': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cod_censo_fgv': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'complemento_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'complemento_original': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ddd_fax': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ddd_telefone1': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'dias_funcionamento': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['biblioteca.DiaFuncionamento']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'endereco_original': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'esfera_administrativa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['biblioteca.EsferaAdministrativa']", 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True', 'blank': 'True'}),
            'ibge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ibge.Municipio']", 'null': 'True', 'db_column': "u'ibge'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'km': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nome_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nome_responsavel': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'numero_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'numero_original': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'periodo_funcionamento': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['biblioteca.PeriodoFuncionamento']", 'null': 'True', 'blank': 'True'}),
            'qtd_emprestimos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_livros_acervo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sniic_n1': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sniic_n2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sniic_n3': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone1': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tipo_esfera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['biblioteca.TipoEsfera']", 'null': 'True', 'blank': 'True'}),
            'tipo_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tipogeo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['territorio.TipoGeo']"})
        },
        u'biblioteca.bibliotecaold': {
            'Meta': {'object_name': 'BibliotecaOLD', 'db_table': "u'biblioteca'"},
            'acervo_liv': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'acesso_usu': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'bairr_orig': ('django.db.models.fields.CharField', [], {'max_length': '26', 'blank': 'True'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '26', 'blank': 'True'}),
            'cep': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cep_orig': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'cod_ibge': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'compl_orig': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'complement': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'ddd_fax': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'ddd_telefo': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'domingo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'end_orig': ('django.db.models.fields.CharField', [], {'max_length': '49', 'blank': 'True'}),
            'esfera_adm': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'id': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '0', 'blank': 'True'}),
            'km': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '0', 'blank': 'True'}),
            'latitude1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '0', 'blank': 'True'}),
            'longitude1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'manha': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'noite': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '83', 'blank': 'True'}),
            'nome_logra': ('django.db.models.fields.CharField', [], {'max_length': '49', 'blank': 'True'}),
            'nome_resp': ('django.db.models.fields.CharField', [], {'max_length': '56', 'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_orig': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'orgao_resp': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'qt_emprest': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'quarta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quinta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sabado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'segunda': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sexta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'sniic_n1': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'sniic_n2': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'sniic_n3': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'tarde': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'terca': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_logra': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        },
        u'biblioteca.diafuncionamento': {
            'Meta': {'object_name': 'DiaFuncionamento'},
            'dia': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'biblioteca.esferaadministrativa': {
            'Meta': {'object_name': 'EsferaAdministrativa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'biblioteca.periodofuncionamento': {
            'Meta': {'object_name': 'PeriodoFuncionamento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'periodo': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'biblioteca.tipoesfera': {
            'Meta': {'object_name': 'TipoEsfera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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

    complete_apps = ['biblioteca']