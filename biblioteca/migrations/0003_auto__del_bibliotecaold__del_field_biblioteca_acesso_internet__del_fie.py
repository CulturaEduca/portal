# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BibliotecaOLD'
        db.delete_table(u'biblioteca')

        # Deleting field 'Biblioteca.acesso_internet'
        db.delete_column(u'biblioteca_biblioteca', 'acesso_internet')

        # Deleting field 'Biblioteca.cep2'
        db.delete_column(u'biblioteca_biblioteca', 'cep2')

        # Deleting field 'Biblioteca.qtd_emprestimos'
        db.delete_column(u'biblioteca_biblioteca', 'qtd_emprestimos')

        # Deleting field 'Biblioteca.qtd_livros_acervo'
        db.delete_column(u'biblioteca_biblioteca', 'qtd_livros_acervo')

        # Deleting field 'Biblioteca.complemento_logradouro'
        db.delete_column(u'biblioteca_biblioteca', 'complemento_logradouro')

        # Deleting field 'Biblioteca.email'
        db.delete_column(u'biblioteca_biblioteca', 'email')

        # Adding field 'Biblioteca.codigo_equipamento'
        db.add_column(u'biblioteca_biblioteca', 'codigo_equipamento',
                      self.gf('django.db.models.fields.IntegerField')(max_length=9, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.cep'
        db.add_column(u'biblioteca_biblioteca', 'cep',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.ddd_telefone2'
        db.add_column(u'biblioteca_biblioteca', 'ddd_telefone2',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.telefone2'
        db.add_column(u'biblioteca_biblioteca', 'telefone2',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.ddd_telefone3'
        db.add_column(u'biblioteca_biblioteca', 'ddd_telefone3',
                      self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.telefone3'
        db.add_column(u'biblioteca_biblioteca', 'telefone3',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.email1'
        db.add_column(u'biblioteca_biblioteca', 'email1',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.email2'
        db.add_column(u'biblioteca_biblioteca', 'email2',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.email3'
        db.add_column(u'biblioteca_biblioteca', 'email3',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.mantenedor'
        db.add_column(u'biblioteca_biblioteca', 'mantenedor',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.cnpj_mantenedor'
        db.add_column(u'biblioteca_biblioteca', 'cnpj_mantenedor',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.codigo_biblioteca'
        db.add_column(u'biblioteca_biblioteca', 'codigo_biblioteca',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.acesso_usuario_internet'
        db.add_column(u'biblioteca_biblioteca', 'acesso_usuario_internet',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Biblioteca.qtd_emprestimos_domiciliar'
        db.add_column(u'biblioteca_biblioteca', 'qtd_emprestimos_domiciliar',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.acervo_livros'
        db.add_column(u'biblioteca_biblioteca', 'acervo_livros',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'BibliotecaOLD'
        db.create_table(u'biblioteca', (
            ('tipo_logra', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('sexta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nome_resp', self.gf('django.db.models.fields.CharField')(max_length=56, blank=True)),
            ('sabado', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=83, blank=True)),
            ('gid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('qt_emprest', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('nome_logra', self.gf('django.db.models.fields.CharField')(max_length=49, blank=True)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=9, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=0, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.GeometryField')(null=True, blank=True)),
            ('quinta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cod_ibge', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=9, blank=True)),
            ('acervo_liv', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('compl_orig', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('segunda', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cep', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('terca', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num_orig', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=0, blank=True)),
            ('sniic_n1', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('sniic_n3', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('sniic_n2', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('bairr_orig', self.gf('django.db.models.fields.CharField')(max_length=26, blank=True)),
            ('ddd_telefo', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('manha', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('noite', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=0, blank=True)),
            ('tarde', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('latitude1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cep_orig', self.gf('django.db.models.fields.CharField')(max_length=9, blank=True)),
            ('esfera_adm', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('ddd_fax', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=26, blank=True)),
            ('complement', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('longitude1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('end_orig', self.gf('django.db.models.fields.CharField')(max_length=49, blank=True)),
            ('quarta', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('acesso_usu', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('domingo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('orgao_resp', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('km', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
        ))
        db.send_create_signal(u'biblioteca', ['BibliotecaOLD'])

        # Adding field 'Biblioteca.acesso_internet'
        db.add_column(u'biblioteca_biblioteca', 'acesso_internet',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Biblioteca.cep2'
        db.add_column(u'biblioteca_biblioteca', 'cep2',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.qtd_emprestimos'
        db.add_column(u'biblioteca_biblioteca', 'qtd_emprestimos',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.qtd_livros_acervo'
        db.add_column(u'biblioteca_biblioteca', 'qtd_livros_acervo',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.complemento_logradouro'
        db.add_column(u'biblioteca_biblioteca', 'complemento_logradouro',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Biblioteca.email'
        db.add_column(u'biblioteca_biblioteca', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Biblioteca.codigo_equipamento'
        db.delete_column(u'biblioteca_biblioteca', 'codigo_equipamento')

        # Deleting field 'Biblioteca.cep'
        db.delete_column(u'biblioteca_biblioteca', 'cep')

        # Deleting field 'Biblioteca.ddd_telefone2'
        db.delete_column(u'biblioteca_biblioteca', 'ddd_telefone2')

        # Deleting field 'Biblioteca.telefone2'
        db.delete_column(u'biblioteca_biblioteca', 'telefone2')

        # Deleting field 'Biblioteca.ddd_telefone3'
        db.delete_column(u'biblioteca_biblioteca', 'ddd_telefone3')

        # Deleting field 'Biblioteca.telefone3'
        db.delete_column(u'biblioteca_biblioteca', 'telefone3')

        # Deleting field 'Biblioteca.email1'
        db.delete_column(u'biblioteca_biblioteca', 'email1')

        # Deleting field 'Biblioteca.email2'
        db.delete_column(u'biblioteca_biblioteca', 'email2')

        # Deleting field 'Biblioteca.email3'
        db.delete_column(u'biblioteca_biblioteca', 'email3')

        # Deleting field 'Biblioteca.mantenedor'
        db.delete_column(u'biblioteca_biblioteca', 'mantenedor')

        # Deleting field 'Biblioteca.cnpj_mantenedor'
        db.delete_column(u'biblioteca_biblioteca', 'cnpj_mantenedor')

        # Deleting field 'Biblioteca.codigo_biblioteca'
        db.delete_column(u'biblioteca_biblioteca', 'codigo_biblioteca')

        # Deleting field 'Biblioteca.acesso_usuario_internet'
        db.delete_column(u'biblioteca_biblioteca', 'acesso_usuario_internet')

        # Deleting field 'Biblioteca.qtd_emprestimos_domiciliar'
        db.delete_column(u'biblioteca_biblioteca', 'qtd_emprestimos_domiciliar')

        # Deleting field 'Biblioteca.acervo_livros'
        db.delete_column(u'biblioteca_biblioteca', 'acervo_livros')


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
            'esfera_administrativa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['biblioteca.EsferaAdministrativa']", 'null': 'True', 'blank': 'True'}),
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
            'tipo_esfera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['biblioteca.TipoEsfera']", 'null': 'True', 'blank': 'True'}),
            'tipo_logradouro': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tipogeo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['territorio.TipoGeo']"})
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