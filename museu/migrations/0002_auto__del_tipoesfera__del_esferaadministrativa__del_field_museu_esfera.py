# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TipoEsfera'
        db.delete_table(u'museu_tipoesfera')

        # Deleting model 'EsferaAdministrativa'
        db.delete_table(u'museu_esferaadministrativa')

        # Deleting field 'Museu.esfera_administrativa'
        db.delete_column(u'museu_museu', 'esfera_administrativa_id')

        # Adding field 'Museu.codigo_equipamento'
        db.add_column(u'museu_museu', 'codigo_equipamento',
                      self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Museu.tipologia_sniic'
        db.add_column(u'museu_museu', 'tipologia_sniic',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sniic.Nivel3'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Museu.codigo_museu'
        db.add_column(u'museu_museu', 'codigo_museu',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Museu.tipo_esfera'
        db.alter_column(u'museu_museu', 'tipo_esfera_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['referencia.TipoEsfera'], null=True))

    def backwards(self, orm):
        # Adding model 'TipoEsfera'
        db.create_table(u'museu_tipoesfera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'museu', ['TipoEsfera'])

        # Adding model 'EsferaAdministrativa'
        db.create_table(u'museu_esferaadministrativa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'museu', ['EsferaAdministrativa'])

        # Adding field 'Museu.esfera_administrativa'
        db.add_column(u'museu_museu', 'esfera_administrativa',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['museu.EsferaAdministrativa'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Museu.codigo_equipamento'
        db.delete_column(u'museu_museu', 'codigo_equipamento')

        # Deleting field 'Museu.tipologia_sniic'
        db.delete_column(u'museu_museu', 'tipologia_sniic_id')

        # Deleting field 'Museu.codigo_museu'
        db.delete_column(u'museu_museu', 'codigo_museu')


        # Changing field 'Museu.tipo_esfera'
        db.alter_column(u'museu_museu', 'tipo_esfera_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['museu.TipoEsfera'], null=True))

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
        u'museu.museu': {
            'Meta': {'object_name': 'Museu'},
            'ano_abertura': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ano_criacao': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'bairro_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'bebedouro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'cep_original': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'codigo_equipamento': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'codigo_museu': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'complemento_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'complemento_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ddd_telefone1': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'endereco_correspondencia': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'endereco_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'estacionamento': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'etiquetas_idioma': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'null': 'True', 'blank': 'True'}),
            'ibge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ibge.Municipio']", 'null': 'True', 'db_column': "u'ibge'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'infra_turista_estrangeiro': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'infra_turista_sinalizacao': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'infra_turistas_etiquetas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'infra_turistas_outros': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'infra_turistas_publicacoes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ingresso_cobrado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'km': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'lanchonete_restaurante': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'livraria': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'local': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'loja': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'medidas_preventivas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medidas_preventivas_brigada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medidas_preventivas_outras': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medidas_preventivas_revisao_extintores': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medidas_preventivas_revisao_rede_eletrica': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medidas_preventivas_treinamento_profissionais': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'nome_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'nome_responsavel': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'numero_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'numero_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'orcamento_proprio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'outras_instalacoes1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'outras_instalacoes2': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'outros_idiomas': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'pne_elevadores_acessiveis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pne_etiquetas_braile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pne_outros_1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pne_outros_2': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pne_rampa_de_acesso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pne_sanitarios_adaptados': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pne_sinalizacao_braile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pne_vagas_exclusivas_estacionamento': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publicacoes_idioma': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'qtd_antropologia_etnografia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_arqueologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_arquivistico': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_artes_visuais': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_bens_acervo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_bens_exatidao': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'qtd_biblioteconomico': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_ciencia_tecnologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_cienciasnaturais_historianatural': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_documental': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_historia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_imagem_som': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_outros': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qtd_virtual': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sanitarios': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sinalizacao_idioma': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'situacao': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'sniic_n1': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sniic_n2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sniic_n3': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone1': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone3': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'telefone_publico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipo_esfera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['referencia.TipoEsfera']", 'null': 'True', 'blank': 'True'}),
            'tipo_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tipogeo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['territorio.TipoGeo']"}),
            'tipologia_sniic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sniic.Nivel3']", 'null': 'True', 'blank': 'True'}),
            'valor_ingresso': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
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

    complete_apps = ['museu']