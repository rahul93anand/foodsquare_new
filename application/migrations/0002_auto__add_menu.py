# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'menu'
        db.create_table(u'application_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rest_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('item_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('available', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'application', ['menu'])


    def backwards(self, orm):
        # Deleting model 'menu'
        db.delete_table(u'application_menu')


    models = {
        u'application.menu': {
            'Meta': {'object_name': 'menu'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rest_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['application']