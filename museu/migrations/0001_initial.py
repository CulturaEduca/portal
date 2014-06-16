# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EsferaAdministrativa'
        db.create_table(u'museu_esferaadministrativa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'museu', ['EsferaAdministrativa'])

        # Adding model 'TipoEsfera'
        db.create_table(u'museu_tipoesfera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'museu', ['TipoEsfera'])

        # Adding model 'Museu'
        db.create_table(u'museu_museu', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('tipogeo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['territorio.TipoGeo'])),
            ('ibge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ibge.Municipio'], null=True, db_column=u'ibge', blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('endereco_original', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('endereco_correspondencia', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
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
            ('ddd_telefone1', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('telefone1', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('telefone2', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('telefone3', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('esfera_administrativa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['museu.EsferaAdministrativa'], null=True, blank=True)),
            ('tipo_esfera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['museu.TipoEsfera'], null=True, blank=True)),
            ('cnpj', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('sniic_n1', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('sniic_n2', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('sniic_n3', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('local', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('ano_criacao', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ano_abertura', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('orcamento_proprio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('qtd_bens_acervo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('qtd_bens_exatidao', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('qtd_antropologia_etnografia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('qtd_arqueologia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('qtd_artes_visuais', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('qtd_cienciasnaturais_historianatural', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('qtd_ciencia_tecnologia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('qtd_historia', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('qtd_imagem_som', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('qtd_virtual', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('qtd_arquivistico', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('qtd_biblioteconomico', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('qtd_documental', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('qtd_outros', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('situacao', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('ingresso_cobrado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('valor_ingresso', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('infra_turista_estrangeiro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('infra_turista_sinalizacao', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sinalizacao_idioma', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('infra_turistas_etiquetas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('etiquetas_idioma', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('infra_turistas_publicacoes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('publicacoes_idioma', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('infra_turistas_outros', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('outros_idiomas', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('bebedouro', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('estacionamento', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lanchonete_restaurante', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('livraria', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('loja', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sanitarios', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('telefone_publico', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('outras_instalacoes1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('outras_instalacoes2', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('pne_vagas_exclusivas_estacionamento', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pne_elevadores_acessiveis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pne_rampa_de_acesso', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pne_sanitarios_adaptados', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pne_sinalizacao_braile', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pne_etiquetas_braile', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pne_outros_1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pne_outros_2', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('medidas_preventivas', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('medidas_preventivas_treinamento_profissionais', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('medidas_preventivas_brigada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('medidas_preventivas_revisao_extintores', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('medidas_preventivas_revisao_rede_eletrica', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('medidas_preventivas_outras', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.GeometryField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'museu', ['Museu'])


    def backwards(self, orm):
        # Deleting model 'EsferaAdministrativa'
        db.delete_table(u'museu_esferaadministrativa')

        # Deleting model 'TipoEsfera'
        db.delete_table(u'museu_tipoesfera')

        # Deleting model 'Museu'
        db.delete_table(u'museu_museu')


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
        u'museu.esferaadministrativa': {
            'Meta': {'object_name': 'EsferaAdministrativa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'complemento_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'complemento_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ddd_telefone1': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'endereco_correspondencia': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'endereco_original': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'esfera_administrativa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['museu.EsferaAdministrativa']", 'null': 'True', 'blank': 'True'}),
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
            'tipo_esfera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['museu.TipoEsfera']", 'null': 'True', 'blank': 'True'}),
            'tipo_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tipogeo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['territorio.TipoGeo']"}),
            'valor_ingresso': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'museu.tipoesfera': {
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

    complete_apps = ['museu']