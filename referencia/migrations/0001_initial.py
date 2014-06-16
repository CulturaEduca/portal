# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Esfera'
        db.create_table(u'referencia_esfera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'referencia', ['Esfera'])

        # Adding model 'TipoEsfera'
        db.create_table(u'referencia_tipoesfera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'referencia', ['TipoEsfera'])


    def backwards(self, orm):
        # Deleting model 'Esfera'
        db.delete_table(u'referencia_esfera')

        # Deleting model 'TipoEsfera'
        db.delete_table(u'referencia_tipoesfera')


    models = {
        u'referencia.esfera': {
            'Meta': {'object_name': 'Esfera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'referencia.tipoesfera': {
            'Meta': {'object_name': 'TipoEsfera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['referencia']