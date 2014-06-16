# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TipoEsfera.esfera'
        db.add_column(u'referencia_tipoesfera', 'esfera',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['referencia.Esfera'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TipoEsfera.esfera'
        db.delete_column(u'referencia_tipoesfera', 'esfera_id')


    models = {
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
        }
    }

    complete_apps = ['referencia']