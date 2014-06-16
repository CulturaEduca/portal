# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'EsferaAdministrativa'
        db.delete_table(u'cinema_esferaadministrativa')

        # Deleting model 'TipoEsfera'
        db.delete_table(u'cinema_tipoesfera')

        # Deleting field 'Cinema.esfera_administrativa'
        db.delete_column(u'cinema_cinema', 'esfera_administrativa_id')

        # Deleting field 'Cinema.ddd'
        db.delete_column(u'cinema_cinema', 'ddd')

        # Adding field 'Cinema.codigo_equipamento'
        db.add_column(u'cinema_cinema', 'codigo_equipamento',
                      self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cinema.ddd_telefone1'
        db.add_column(u'cinema_cinema', 'ddd_telefone1',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cinema.ddd_telefone2'
        db.add_column(u'cinema_cinema', 'ddd_telefone2',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cinema.ddd_telefone3'
        db.add_column(u'cinema_cinema', 'ddd_telefone3',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cinema.ddd_fax'
        db.add_column(u'cinema_cinema', 'ddd_fax',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cinema.fax'
        db.add_column(u'cinema_cinema', 'fax',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cinema.tipologia_sniic'
        db.add_column(u'cinema_cinema', 'tipologia_sniic',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sniic.Nivel3'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cinema.codigo_cinema'
        db.add_column(u'cinema_cinema', 'codigo_cinema',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Cinema.tipo_esfera'
        db.alter_column(u'cinema_cinema', 'tipo_esfera_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['referencia.TipoEsfera'], null=True))

    def backwards(self, orm):
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

        # Adding field 'Cinema.esfera_administrativa'
        db.add_column(u'cinema_cinema', 'esfera_administrativa',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cinema.EsferaAdministrativa'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cinema.ddd'
        db.add_column(u'cinema_cinema', 'ddd',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Cinema.codigo_equipamento'
        db.delete_column(u'cinema_cinema', 'codigo_equipamento')

        # Deleting field 'Cinema.ddd_telefone1'
        db.delete_column(u'cinema_cinema', 'ddd_telefone1')

        # Deleting field 'Cinema.ddd_telefone2'
        db.delete_column(u'cinema_cinema', 'ddd_telefone2')

        # Deleting field 'Cinema.ddd_telefone3'
        db.delete_column(u'cinema_cinema', 'ddd_telefone3')

        # Deleting field 'Cinema.ddd_fax'
        db.delete_column(u'cinema_cinema', 'ddd_fax')

        # Deleting field 'Cinema.fax'
        db.delete_column(u'cinema_cinema', 'fax')

        # Deleting field 'Cinema.tipologia_sniic'
        db.delete_column(u'cinema_cinema', 'tipologia_sniic_id')

        # Deleting field 'Cinema.codigo_cinema'
        db.delete_column(u'cinema_cinema', 'codigo_cinema')


        # Changing field 'Cinema.tipo_esfera'
        db.alter_column(u'cinema_cinema', 'tipo_esfera_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cinema.TipoEsfera'], null=True))

    models = {
        u'cinema.cinema': {
            'Meta': {'object_name': 'Cinema'},
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'bairro_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'cep_original': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'codigo_cinema': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'codigo_equipamento': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'complemento_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'complemento_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ddd_fax': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ddd_telefone1': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ddd_telefone2': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ddd_telefone3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'endereco_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
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
            'tipo_esfera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['referencia.TipoEsfera']", 'null': 'True', 'blank': 'True'}),
            'tipo_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tipogeo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['territorio.TipoGeo']"}),
            'tipologia_sniic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sniic.Nivel3']", 'null': 'True', 'blank': 'True'})
        },
        u'cinema.grupoancine': {
            'Meta': {'object_name': 'GrupoAncine'},
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

    complete_apps = ['cinema']