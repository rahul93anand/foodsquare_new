# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'orderplaced.status'
        db.add_column(u'application_orderplaced', 'status',
                      self.gf('django.db.models.fields.CharField')(default='Order Placed', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'orderplaced.status'
        db.delete_column(u'application_orderplaced', 'status')


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
            'status': ('django.db.models.fields.CharField', [], {'default': "'Order Placed'", 'max_length': '30'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['application']