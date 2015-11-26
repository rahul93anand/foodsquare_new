# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'orderplaced.order_id'
        db.alter_column(u'application_orderplaced', 'order_id', self.gf('django.db.models.fields.CharField')(max_length=40))

    def backwards(self, orm):

        # Changing field 'orderplaced.order_id'
        db.alter_column(u'application_orderplaced', 'order_id', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'application.menu': {
            'Meta': {'object_name': 'menu'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rest_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'application.orderplaced': {
            'Meta': {'object_name': 'orderplaced'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'order_id': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'placed_on': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['application']